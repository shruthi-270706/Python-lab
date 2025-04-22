def find_smallest_element():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    print("Enter the matrix elements row-wise:")
    for i in range(rows):
        row=[]
        for j in range(cols):
            num=int(input())
            row.append(num)
        matrix.append(row)
    print(matrix)
    smallest=matrix[0][0]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]<=smallest:smallest=matrix[i][j]
    print(smallest)
find_smallest_element()