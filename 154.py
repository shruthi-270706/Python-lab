l1=[]
l2=[]
num1=int(input("Enter the number of numbers: "))
for i in range(num1):
    n1=int(input("Enter the number: "))
    l1.append(n1)
print(l1)
s1=set(l1)
num2=int(input("Enter the number of numbers: "))
for i in range(num2):
    n2=int(input("Enter the number: "))
    l2.append(n2)
print(l2)
s2=set(l2)
union=s1.union(s2)
print(union)