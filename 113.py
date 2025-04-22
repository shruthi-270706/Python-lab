row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of cols: "))
A=[]
for i in range(row):
    rows=[]
    for j in range(col):
        num=int(input("Enter the numbers: "))
        rows.append(num)
    A.append(rows)
print("The Given Matrix is: ")
for i in range(row):
    for j in range(col):
        print(A[i][j],end=' ')
    print()
print("Lower Triangle Matrix is:" )
for i in range(row):
    for j in range(col):
        if i>=j:print(A[i][j],end=' ')
        else: print(" ",end=" ")
    print()