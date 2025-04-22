num=int(input("Enter the number of elements: "))
t1=[]
for i in range(num):
    num=int(input("Enter the number: "))
    t1.append(num)
t2=tuple(t1)
print("The Tuple is:",t2)
maximum=max(t1)
minimum=min(t1)
print(f"Maximum:{maximum}, Minimum:{minimum}")