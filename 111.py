def maximum(A):
    if len(A)==1:return A[0]
    max_num=maximum(A[1:])
    if A[0]>max_num:return A[0]
    else:return max_num
num=int(input("Enter the numbers of elements: "))
A=[]
for i in range(num):
    A.append(int(input("Enter a number: ")))
print(maximum(A))