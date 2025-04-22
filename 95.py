def integer(num):
    temp = num
    position = 1 
    while temp > 0:
        count = 0
        rem = temp % 10 
        if position % 2 == 0:
            for i in range(1, rem + 1):
                if rem % i == 0:
                    count += 1
            if count == 2:print(f"Digit {rem} at position {position} is Prime")
            else:print(f"Digit {rem} at position {position} is Not Prime")
        temp //= 10  
        position += 1  
num = int(input("Enter the 10-digit number: "))
integer(num)