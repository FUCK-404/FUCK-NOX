
from os import system
import time
import os
from platform import machine
print('Checking For Update...')
system('git pull')
time.sleep(2)
print(' Follow My Facebook Account Update bruh...')
os.system('xdg-open https://www.facebook.com/tera.crush.69k')
if machine()=='aarch64':
    import nox
    nox.main()
else:
    import nox32
    nox32.main()
bit = platform.architecture()[0]
if bit == '64bit':
    import nox
    nox.main
elif bit == '32bit':
    import nox32
    nox32.main()
