import max_number
num=int(input("Enter the number of elements: "))
l1=[]
for i in range(num):
    n=int(input("Enter the number: "))
    l1.append(n)
highest_number1=max_number.highest_number(l1)
print(highest_number1)