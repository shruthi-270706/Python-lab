l1=[]
num=int(input("Enter the number of items: "))
for i in range(num):
    price=int(input("Enter the item price: "))
    l1.append(price)
t1=tuple(l1)
print(f"Lowest Price: {min(t1)}")