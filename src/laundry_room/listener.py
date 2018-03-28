import socket
from struct import unpack
from threading import Thread
from collections import namedtuple
from time import monotonic

_HISTORY_LEN_SEC = 5
_POWER_THRESHOLD = 200
_N_FLOORS = 19


class _Default(object):
    def __repr__(self):
        return '(' + ', '.join(
            str(getattr(self, key)) for key in self.__dict__ if not key.startswith('_')) + ')'

    def __eq__(self, other):
        try:
            return all(getattr(self, key) == getattr(other, key)
                       for key in self.__dict__ if not key.startswith('_'))
        except AttributeError:
            return False


_Value = namedtuple('Value', 'time value')


class _History(_Default):
    def __init__(self):
        self._sum = 0
        self._values = []

    def _remove_old_values(self, cur_time=monotonic()):
        while self._values and cur_time - self._values[0].time > _HISTORY_LEN_SEC:
            self._sum -= self._values.pop(0).value

    def add(self, value):
        cur_time = monotonic()
        self._remove_old_values(cur_time)
        self._values.append(_Value(cur_time, value))
        self._sum += value

    def avg(self):
        self._remove_old_values()
        n_values = len(self._values)
        if n_values == 0:
            return 0
        return self._sum / n_values


class _Floor(_Default):
    def __init__(self):
        self.wm = _History()
        self.drier = _History()


class Listener(object):
    def __init__(self):
        self._stop_flag = False
        self._thread = Thread(target=self._thread_listener_loop)
        self._thread.daemon = True

    def _init_db(self):
        import itertools
        for floor, type_id in itertools.product(range(0, _N_FLOORS), ['WM', 'DR']):
            self._update_db(floor, type_id, 0)

    def _update_db(self, floor_id, machine, status):
        from laundry_room import models
        from common.models import Floor
        from django.utils import timezone

        floor_obj, created = Floor.objects.get_or_create(id=floor_id)
        if created:
            floor_obj.save()
        machine_obj, created = models.Machine.objects.get_or_create(kind_of=machine, floor=floor_obj)

        if machine_obj.status is not status:
            floor_obj.last_query_time = timezone.now()
            floor_obj.save()

            machine_obj.status = status
            machine_obj.save()

    def _check_threshold(self, old_avg, avg):
        if avg < _POWER_THRESHOLD and old_avg >= _POWER_THRESHOLD:
            # print(msg.format('off'))
            return 0  # off
        elif avg >= _POWER_THRESHOLD and old_avg < _POWER_THRESHOLD:
            # print(msg.format('on'))
            return 1  # on
        return None

    def _thread_listener_loop(self):
        floors = [_Floor() for _ in range(_N_FLOORS)]

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.bind(('', 1234))

        while not self._stop_flag:
            try:
                data, (address, port) = sock.recvfrom(68)
                floor_num = address.split('.')[-1]  # last octett of IP is the level number
                drier_power, wm_power = unpack('>HH', data[4:8])

                floor = floors[int(floor_num)]
                wm = floor.wm
                drier = floor.drier
                for machine, power, type_id in [(wm, wm_power, 'WM'), (drier, drier_power, 'DR')]:
                    old_avg = machine.avg()
                    machine.add(power)
                    status = self._check_threshold(old_avg, machine.avg())

                    if status is not None:
                        self._update_db(floor_num, type_id, status)

            except socket.timeout:
                print('Timeout...')

    def start(self):
        print('Start listener thread')
        self._thread.start()

    def stop(self):
        print('THREAD STOP!')
        self._stop_flag = True
        self._thread.join()
        print('JOINED')
