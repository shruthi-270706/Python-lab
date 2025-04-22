employee={}
num=int(input("Enter the number of employees: "))
for i in range(num):
    e_id=input("Enter Employees ID: ")
    name=input("Enter Employees Name: ")
    salary=int(input("Enter Employess Salary: "))
    employee[e_id]=[name,salary]
print(employee)
def add():
    e_id=input("Enter Employee ID: ")
    if e_id in employee:
        print(f"{e_id} is already an employee")
    else:
        name=input("Enter Employee Name: ")
        salary=int(input("Enter Employees Salary: "))
        employee[e_id]=[name,salary]
        print(f"{e_id} is added as Employee")
def update_salary():
    e_id=input("Enter Employees ID: ")
    if e_id in employee:
        salary=int(input("Enter the salary: "))
        l=employee[e_id]
        l[1]=salary
        employee[e_id]=l
        print(f"{e_id} is updated with {salary}")
    else:print(f"{e_id} is not an Employee")
def hl_salary():
    maxSal = float('-inf')
    minSal = float('inf')
    for key in employee.keys():
        l = employee[key]
        if maxSal < l[1]:
            maxSal = l[1]
        if minSal > l[1]:
            minSal = l[1]
    print(f"Highest salary: {maxSal}")
    print(f"Lowest Salary: {minSal}")
def average():
    sum=0
    for key in employee.keys():
        l=employee[key]
        sum+=l[1]
    print(f"Employees salary of employees is: {sum/len(employee)}")
def end_program():
    print("EXIT")
    exit()
while True:
    print("\n1:Add\n2:Update salary\n3:Highest & Lowest \n4:Average")
    choice=int(input("Enter your choice: "))
    if choice==1:add()
    elif choice==2:update_salary()
    elif choice==3:
        hl_salary()
    elif choice==4:average()
    elif choice==5:end_program()