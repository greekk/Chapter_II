import os
workdir = r'C:\Users\a.grichuk\Desktop\current_work\eskaliev\new2\album1'
files = os.listdir(workdir)

# files = map(lambda file: os.path.join(workdir, file), files)
files = [os.path.join(workdir, path) for path in files]
print(files)
for path in files:
    if os.path.basename(path) == 'Thumbs.db':
        continue
print(path)
