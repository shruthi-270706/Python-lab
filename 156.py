num=int(input("Enter the number of students: "))
l1=[]
for i in range(num):
    marks=int(input("Enter the marks: "))
    l1.append(marks)
t1=tuple(l1)
print(t1)
print(f"Average of total marks: {sum(t1)/len(t1)}")