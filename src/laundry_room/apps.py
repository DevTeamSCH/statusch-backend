import fcntl
import atexit
from django.apps import AppConfig
from laundry_room.listener import Listener

class LaundryRoomConfig(AppConfig):
    name = 'laundry_room'

    def __init__(self, app_name, app_module):
        AppConfig.__init__(self, app_name, app_module)
        self._lock_file = None

    def ready(self):
        print('New app process')
        self._lock_file = open('./lock', 'w')
        try:
            fcntl.flock(self._lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            listener = Listener()
            listener.start()
            atexit.register(listener.stop)
        except BlockingIOError:
            pass
