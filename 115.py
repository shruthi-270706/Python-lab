def details():
    num=int(input("Enter the number of students: "))
    total_marks,total_sub=0,0
    list1=[]
    for i in range(num):
        name=input("Enter name: ")
        htno=input("Enter Hallticket number: ")
        while True:
            marks = input("Enter marks of 5 subjects (by giving space): ").split()
            if all(m.isdigit() for m in marks):
                list2 = [int(m) for m in marks]
                if all(0 <= m <= 100 for m in list2):
                    break
            print("Invalid input. Please enter valid integers between 0 and 100.")
        list1.append(name)
        list1.append(htno)
        list1.extend(list2)
    total_marks+=sum(list2)
    total_sub+=len(list2)
    average=total_marks/total_sub
    if average>=90 and average<=100:Grd = "A"
    elif average<90 and average>=80:Grd = "B"
    elif average<80 and average>=70:Grd = "C"
    elif average<70 and average>=60:Grd = "D"
    else :Grd = "FAIL"
    list1.append(Grd)
    maximum=max(list2)
    list1.append(maximum)
    percentage=(sum(list2)/500*100)
    list1.append(percentage)
    new_name=input("Enter the new name: ")
    list1[0]=new_name
    print("**************************")
    print(f"Name: {list1[0]}\nHTNO: {list1[1]}\nMarks of 5th sub: {list1[6]}")
    print(f"Maximum: {maximum}\nPercentage: {percentage:.2f}%")
details()
