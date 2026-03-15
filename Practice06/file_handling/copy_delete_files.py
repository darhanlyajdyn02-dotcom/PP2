import shutil
import os

text = "for_test.txt"
shutil.copy(text,"for_test_copy.txt")
print("file copied")

if os.path.exists("for_test_copy.txt"):
    os.remove("for_test_copy.txt")
    print("file deleted")
else:
    print("file not found")