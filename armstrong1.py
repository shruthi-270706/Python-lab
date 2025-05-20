import sys
if len(sys.argv) > 1:
    num = int(sys.argv[1])
    temp1 =temp2= num
    count = sum = 0
    while temp1 > 0:
        temp1 //= 10
        count += 1
    while temp2 > 0:
        rem = temp2 % 10
        sum += rem ** count  
        temp2 //= 10
    if num == sum:print("Armstrong")
    else:print("Not an Armstrong")
else:print("Invalid input")

