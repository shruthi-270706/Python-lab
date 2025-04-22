def sum(num):
    digit_sum=0
    if num==0: return 0
    else:
        return num%10+sum(num//10)
num=int(input("Enter the number: "))
print(sum(num))