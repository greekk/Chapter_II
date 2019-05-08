import sys

print(sys.argv)

print(sys.executable)

# sys.exit(0)
for path in sys.path:
    print(path)

os = sys.platform
if os=='win32':
    print("You are have a Windows!!!!")
    import _winreg

