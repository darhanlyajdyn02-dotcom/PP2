class person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class Student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation = year
    def grt(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduation)

s = Student("Aydyn","Darkhanuly",2025)
s.grt()

