sum_even = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    if num % 2 == 0:
        sum_even += num
print("Sum of all even numbers entered:", sum_even)
