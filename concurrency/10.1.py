import subprocess

try:
    completed = subprocess.run(['powershell','Get-ChildItem',], check=True, stdout=subprocess.PIPE)
    print('returncode: ', completed.returncode)
    print("Have {} bytes in stdout: \n{}".format(len(completed.stdout), completed.stdout.decode('cp866')))
except subprocess.CalledProcessError as err:
    print("Error: ", err)
except Exception as ex:
    print(ex)
