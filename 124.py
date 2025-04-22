num1=int(input("Enter the number of numbers: "))
s1=[]
for i in range(num1):
    num1=int(input("Enter the number: "))
    s1.append(num1)
s2=set(s1)
num2=int(input("Enter the number of numbers: "))
s3=[]
for i in range(num2):
    num2=int(input("Enter the number: "))
    s3.append(num2)
s4=set(s3)
print("Elements in the set1: ",s2)
print("Elements in the set2: ",s4)
union=s2 | s4
print("Union of sets: ",union)
intersection=s2 & s4
print("Intersection of sets: ",intersection)
difference=s2-s4
print("The difference is: ",difference)
set_symmetric=s2-s4 | s4-s2
print("Set Symmetric: ",set_symmetric)
subset=s2.issubset(s4)
print(subset)