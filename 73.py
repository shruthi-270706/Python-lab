def is_perfect_number(n):
    sum= 0
    for i in range(1, n):
        if n % i == 0:sum+= i
    return sum== n
smallest=None
while True:
    num=int(input("Enter the numbers(-1 to stop):"))
    if (num==-1):break
    if smallest is None or (num<smallest):smallest=num
if smallest is not None:
    if is_perfect_number(smallest):print("Smallest number is a perfect number")
    else:print("Smallest number is not a perfect number")