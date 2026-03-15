file = "for_test.txt"

with open(file,"a") as f:
    f.write("\nNew line is for append \n")

with open(file,"r") as f:
    print(f.read())