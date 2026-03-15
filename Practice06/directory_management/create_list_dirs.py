import os

os.makedirs("dir1/dir2/dir3", exist_ok = True)
print("directories created")

print("Contents of the current directory:",os.listdir("."))