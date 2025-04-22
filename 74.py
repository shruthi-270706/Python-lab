def perfect(number):
    sum=0
    for i in range(1,number):
        if(number%i)==0:sum+=i
    return sum==number
number=int(input("Enter the number:"))
print(perfect(number))