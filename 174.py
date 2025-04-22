num1=int(input("Enter the numebr of elements: "))
l1=[]
l2=[]
for i in range(num1):
    n1=(input("Enter the number: "))
    l1.append(n1)
num2=int(input("Enter the number of elements: "))
for i in range(num2):
    n2=(input("Enter the number: "))
    l2.append(n2)
s1=set(l1)
s2=set(l2)
set_symmetric1=s1.symmetric_difference(s2)
print(set_symmetric1)