import subprocess
import time
shell = "powershell.exe"
process = subprocess.Popen([shell, ])
process.wait()
# programs = ["ping 10.10.105.246", "ping 10.10.105.247"]
#
# for program in programs:
#     subprocess.Popen(program)
args = ["ping", "10.10.105.246"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
for line in data:
    try:
        print(line.decode("cp866"))
    except AttributeError:
        print("AttributeError!!")

