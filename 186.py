class Parent1:
    amt1 = 10000
    def display1(self):
       print("Amount From Parent1: ", self.amt1)
       return self.amt1
class Parent2:
    amt2 = 20000
    def display2(self):
       print("Amount From Parent2: ", self.amt2)
       return self.amt2
class Child(Parent1, Parent2):
    print("Amount the child has: ", obj.amt3)
    amt3 = 2000
obj = Child()
print("Amount the child has: ", obj.amt3)
print("Total amount = ", obj.display1() + obj.display2() + obj.amt3)