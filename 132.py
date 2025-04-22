num1 = int(input("Enter the number of elements in set1: "))
s1 = []
for i in range(num1):
    ele1 = int(input("Enter the number: "))
    s1.append(ele1)
s2 = set(s1) 
num2 = int(input("Enter the number of elements in set2: "))
s3 = []
for i in range(num2):
    ele2 = int(input("Enter the number: "))
    s3.append(ele2)
s4 = set(s3) 
print("Set1:", s2)
print("Set2:", s4)
if s2.issubset(s4):print("Set1 is a subset of Set2")
else:print("Set1 is not a subset of Set2")
if s2.isdisjoint(s4):print("Set1 is disjoint from Set2")
else:print("Set1 is not disjoint from Set2")
if s2.intersection(s4):print("Set1 intersects with Set2")
else:print("Set1 does not intersect with Set2")