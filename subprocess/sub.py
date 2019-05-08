import subprocess

code = subprocess.call("notepad.exe")
if code == 0:
    print('success!!')
else:
    print('Error!!')
    

