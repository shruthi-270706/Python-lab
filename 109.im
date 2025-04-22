def details():
    num=int(input("Enter the number of students: "))
    total_marks,total_sub=0,0
    list1=[]
    for i in range(num):
        name=input("Enter name: ")
        htno=input("Enter Hallticket number: ")
        while True:
            marks = input("Enter marks of 3 subjects (by giving space): ").split()
            if all(m.isdigit() for m in marks):
                list2 = [int(m) for m in marks]
                if all(0 <= m <= 100 for m in list2):
                    break
            print("Invalid input. Please enter valid integers between 0 and 100.")
        list1.append(name)
        list1.append(htno)
        list1.extend(list2)
    print(list1)
    total_marks+=sum(list2)
    total_sub+=len(list2)
    average=total_marks/total_sub
    print(average)
    if average>=90 and average<=100:Grd = "A"
    elif average<=90 and average>=80:Grd = "B"
    elif average<=80 and average>=70:Grd = "C"
    elif average<=70 and average>=60:Grd = "D"
    else :Grd = "FAIL"
    list1.append(Grd)
    maximum=max(list2)
    list1.append(maximum)
    print(list1)
    print(f"Name: {list1[0]}\nHTNO: {list1[1]}\nM1: {list1[2]}")
    print(f"M2: {list1[3]}\nM3: {list1[4]}\nMaximum: {maximum}")
    print(f"Grade: {Grd}")
details()