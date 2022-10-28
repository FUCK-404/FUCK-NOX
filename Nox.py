from os import system
import time
from platform import machine
print('Checking For Update...')
system('git pull')
time.sleep(2)
if machine()=='aarch64':
    
    import nox.so
    nox.main

    
    
