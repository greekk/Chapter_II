import subprocess
from sys import sys

print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

code = subprocess.call(['ping.exe', '192.168.40.126'])
print("resultcode is: ", code)
