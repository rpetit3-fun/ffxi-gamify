#!/usr/bin/env python
import os
import sys
import socket

if __name__ == "__main__":
    settings = 'darkstartools.settings.local'
    if socket.gethostname() is not 'ffxi-server':
        settings = 'darkstartools.settings.remote'

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
