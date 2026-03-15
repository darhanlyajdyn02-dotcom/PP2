import os
import shutil

os.makedirs("dir1/dir2",exist_ok = True)
shutil.copy("sample.txt", "dir1/dir2/sample.txt")
print("file copied to dir1/dir2")