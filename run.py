import os
import sys
try:
    command = sys.argv[1]
    if command == 'shutdown':
        os.system('"G:\my\mine\\noder\OSTool\cmd\shutdown.cmd"')
except IndexError:
    pass