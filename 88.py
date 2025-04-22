def students(name,**details):
    print(name)
    if details:
        for key,value in details.items():
            print(key,value)
    else:print("no")
name = input("Enter student name: ")
age = input("Enter age (or press enter to skip): ")
course = input("Enter course (or press enter to skip): ")
students(name,age=age if age else None ,course=course if course else None)