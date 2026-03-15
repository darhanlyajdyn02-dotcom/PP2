file = "for_test.txt"

text = """Hello, this is a sample text.
This file is used for practice.
Python makes working with files easy."""

with open(file,"w") as f:
    f.write(text)

with open(file,"r") as f:
    content = f.read()
    print(content)