def check_digits(num, i=1, count=0, rem=None):
    if num == 0 and rem is None:  
        return  
    if rem is None:  
        rem = num % 10  
    if i > rem:  
        print("Prime" if count == 2 and rem > 1 else "Not a prime")  
        check_digits(num // 10)  
        return  
    check_digits(num, i + 1, count + (rem % i == 0), rem)  
num = int(input("Enter the 10-digit number: "))  
check_digits(num)