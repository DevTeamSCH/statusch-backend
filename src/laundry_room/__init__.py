import sys


if "migrate" not in sys.argv and "makemigrations" not in sys.argv:
    default_app_config = "laundry_room.apps.LaundryRoomConfig"
