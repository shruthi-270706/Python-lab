def highestsalary():
    employee={}
    num=int(input("Enter the number of employees: "))
    for i in range(num):
        name=input("Enter Employees Name: ")
        salary=int(input("Enter Employess Salary: "))
        employee[name]=salary
    print(employee)
    max_salary=max(employee.values())
    for name , salary in employee.items():
        if salary==max_salary:
            print(f"{name}:{max_salary}")
highestsalary()