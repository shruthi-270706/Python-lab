row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of cols: "))
sum=0
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
for i in range(row):
    for j in range(col):
        if i==j:sum+=A[i][j]
print(f"The sum of Diagonals is:{sum}")