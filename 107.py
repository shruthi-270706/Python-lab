def factorial(num):
    if num==0:return 1
    mul=1
    for i in range(1,num+1):
        return num*factorial(num-1)
num=int(input("Enter the number: "))
print(factorial(num))