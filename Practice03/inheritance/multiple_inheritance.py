
class Mother:
    def eye_color(self):
        return "blue eyes"
    
    def skill1(self):
        return "Very well in cooking"

class Father:
    def hair_color(self):
        return "Black hair"
    
    def skill2(self):
        return "Very well in work"

class Child(Mother, Father):
    def my_features(self):
        return f"I have {self.eye_color()} and {self.hair_color()}"

child = Child()

print(child.eye_color())   
print(child.hair_color())  
print(child.skill1())     
print(child.skill2())      
print(child.my_features())  