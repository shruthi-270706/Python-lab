from vehicle.car_information import car ,truck
print("1:Car Details\n2:Truck Details ")
choice=int(input("Enter Your choice: "))
if choice==1:
    details1={}
    num=int(input("Enter the number of cars: "))
    for i in range(num):
        name=input("Enter the Model name: ")
        speed=int(input("Enter the Speed of the car: "))
        details1[name]=speed
    cars=car(details1)
    print(cars)
elif choice==2:
    details2={}
    num=int(input("Enter the number of cars: "))
    for i in range(num):
        name=input("Enter the Model name: ")
        speed=int(input("Enter the Speed of the truck: "))
        details2[name]=speed
    trucks=truck(details2)
    print(trucks)