class Parent: 
   def _init_(self,name):
     self.name = name
   def getName(self):
     return self.name
class Child(Parent): 
   def _init_(self,name,age):
     Parent._init_(self,name)
     self.age = age
   def getAge(self):
     return self.age
class Grandchild(Child):
   def _init_(self,name,age,location):
     Child._init_(self,name,age)
     self.location=location
   def getLocation(self):
     return self.location
gc = Grandchild("Srujan",18,"Hyderabad")
print(gc.getName(), gc.getAge(), gc.getLocation())