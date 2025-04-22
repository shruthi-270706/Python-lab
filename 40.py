signal=str(input("Enter light colour as input(R,Y,G): "))
if(signal=='r' or signal=='R'): print("The Vehicle must stop")
elif(signal=='y' or signal=='Y'):
    print("The vehicle should slow down and prepare to stop")
elif(signal=='g' or signal=='G'):
    print("The Vehicle can go")
else :print("Invalid input")