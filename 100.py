def is_prime(n):
    if n < 2:return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:return False
    return True
def check_even_positions(num, position=2):
    if num == 0:return
    num=num//10
    rem = num % 10  
    if is_prime(rem):print(f"Digit {rem} at position {position} is Prime")
    else:print(f"Digit {rem} at position {position} is Not Prime")
    check_even_positions(num // 10, position + 2)
num = int(input("Enter a 10-digit integer number: "))
temp = str(num)
if len(temp) == 10:
    num = int(temp[::-1]) 
    check_even_positions(num)
else:print("Please enter only a 10-digit number")