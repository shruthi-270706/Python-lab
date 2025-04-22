num=int(input("Enter the number of students: "))
students={}
for i in range(num):
    name=input("Enter the name: ")
    salary=int(input("Enter the salary: "))
    students[name]=salary
print(students)
lowest_salary=min(students.values())
for name , salary in students.items():
    if salary==lowest_salary:
        print(f"{name}:{lowest_salary}")
        break