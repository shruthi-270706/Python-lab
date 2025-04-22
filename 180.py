import random
n1=int(input("Enter the start number: "))
n2=int(input("Enter the End number: "))
n3=int(input("Enter how many numbers you want: "))
file_name=input("Enter file name: ")
open("prime.txt","w").close()
open("perfect.txt","w").close()
open("Armstrong.txt","w").close()
open("strong.txt","w").close()
open("normal_number.txt","w").close()
open(file_name,"w").close()
for i in range(n3+1):
    number=random.randint(n1,n2)
    with open(file_name,"a") as file:
        file.write(f"{number}\n")
with open(file_name,'r') as f:
    for line in f:
        number=int(line.strip())
        printed = False
        if number > 1:
            for j in range(2, number):
                if number % j == 0:
                    break
            else:
                print(f"{number} is Prime")
                with open("prime.txt","a") as prime:
                    prime.write(f"{number}\n")
                continue
        temp=number
        sum1=0
        for j in range(1, number):
            if number % j == 0:
                sum1 += j
        if sum1 == number and number != 0:
            print(f"{number} is Perfect")
            with open("perfect.txt","a") as perfect:
                perfect.write(f"{number}\n")
            printed = True
        temp1 = temp2 = number
        count = 0
        while temp1 > 0:
            temp1 //= 10
            count += 1
        sum2 = 0
        while temp2 > 0:
            rem = temp2 % 10
            sum2 += rem**count
            temp2 //= 10
        if sum2 == number:
            print(f"{number} is Armstrong")
            with open("Armstrong.txt","a") as arm:
                arm.write(f"{number}\n")
            printed = True
        temp = number
        sum3 = 0
        while temp > 0:
            digit = temp % 10
            fact = 1
            for i in range(1, digit + 1):
                fact *= i
            sum3 += fact
            temp //= 10
        if sum3 == number:
            print(f"{number} is Strong")
            with open("strong.txt","a") as strong:
                strong.write(f"{number}\n")
            printed = True
        if not printed:
            print(f"{number} is Normal")
            with open("normal_number.txt","a") as normal:
                normal.write(f"{number}\n")N