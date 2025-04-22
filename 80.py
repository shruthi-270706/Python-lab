def factorial(number):
    sum=count=0
    fact=1
    temp=number
    for i in range(1,number+1):fact*=i
    print("The factorial of number is: ",fact)
    if (fact>=100):
        for i in range(1,fact+1):
            if (fact%i)==0:count+=1
        if(count==2):print("It is greater than 100 and prime number")
        else:print("It is greater than 100 but not a prime number")
    else:
        for i in range(1,fact):
            if (fact%i)==0:sum+=i
        if(fact==sum):print("It is lessthan 100 and perfect number")
        else:print("It is less than 100 but not perfect number")
number=int(input("Enter the number:"))
factorial(number)