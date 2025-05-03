num=int(input("Enter the no.of elements: "))
A=[]
for i in range(num):
    A.append(int(input("Enter the number: ")))
print(A)
find=int(input("Enter the number you want to find: "))
count=0
for i in range(num):
    if find==A[i]:
        count+=1
        break
if count>=1:print(f"Yes! It is present at Index{[i+1]}")
else:print("It is not present in the list")
