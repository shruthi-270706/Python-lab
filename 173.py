num=int(input("Enter the number of students: "))
students={}
for i in range(num):
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    students[name]=age
print(students)
first=second=float("-inf")
for youngest in students.values():
    if youngest>first:
        second=first
        first =youngest
    elif youngest>second and youngest!=first: second=youngest
for name, youngest in students.items():
    if youngest==second:
        print(f"{name}:{second}")
        break