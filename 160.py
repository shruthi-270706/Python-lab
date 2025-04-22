l1=[]
num=int(input("Enter the number of temperatures: "))
for i in range(num):
    temp=int(input("Enter the temperature: "))
    l1.append(temp)
t1=tuple(l1)
print(f"Highest Temperature: {max(t1)}")