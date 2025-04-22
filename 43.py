position=str(input("Enter the position(1,2,3): "))
experience=int(input("Enter the age of experience: "))
Ms,Ds,Is=5000,4000,1500
if(position=='1'):
    if(experience>=5):bonus=20
    elif(1<=experience<5):bonus=10
    else: bonus=0
    Ms=Ms+(Ms*bonus/100)
    print("Your salary is:",Ms)
elif(position=='2'):
    if(experience>=5):bonus=20
    elif(1<=experience<5):bonus=10
    else: bonus=0
    Ds=Ds+(Ds*bonus/100)
    print("Your salary is:",Ds)
elif(position=='3'):
    if(experience>=5):bonus=20
    elif(1<=experience<5):bonus=10
    else: bonus=0
    Is=Is+(Is*bonus/100)
    print("Your salary is:",Is)