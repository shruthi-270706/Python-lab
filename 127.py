num1=int(input("Enter the number of elements: "))
s1=[]
for i in range(num1):
    num1=int(input("Enter the numbers: "))
    s1.append(num1)
s2=set(s1)
num2=int(input("Enter the number of elements: "))
s3=[]
for i in range(num2):
    num2=int(input("Enter the numbers: "))
    s3.append(num2)
s4=set(s3)
if s4.issubset(s2):print("Set B is a subset of Set A")
else:print("Set B is NOT a subset of Set A")
if s2.issuperset(s4):print("Set A is a superset of Set B")
else:print("Set A is NOT a superset of Set B")