#!/usr/bin/python3

from . import chaff
from . import debug
from . import vsftpdbd

MODULES =   [
#             chaff.Chaff(),
#             debug.Debug(), # Uncomment this to test if the loader is working
             vsftpdbd.VSFTPdBackdoor(),
            ]