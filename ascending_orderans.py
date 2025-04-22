import ascending_order
num1=int(input("Enter the numebr of elements: "))
l1=[]
for i in range(num1):
    n1=int(input("Enter the number: "))
    l1.append(n1)
proper_list=ascending_order.shuffle(l1)
print(proper_list)