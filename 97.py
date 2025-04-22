rows = int(input("Enter the number of rows: "))
ch = 'A'
count = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1, rows + 1):
    for j in range(i):
        print(alphabet[count], end=" ")
        count += 1
    print()
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print(alphabet[count], end=" ")
        count += 1
    print()