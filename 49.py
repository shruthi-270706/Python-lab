num = int(input("Enter the number of rows: "))
a, b = 0, 1
for i in range(1, num + 1):
    for _ in range(i):
        print(a, end=" ")  
        a, b = b, a + b 
    print()  