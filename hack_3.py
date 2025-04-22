def is_prime(n1):
    if n1<2:return False
    for i in range(2, n1):
        if n1%i==0:return False
    return True
def is_perfect(n1):
    total=0
    for i in range(1, n1):
        if n1% i==0:total += i
    return total==n1
def is_armstrong(n1):
    temp1 = temp2 = n1
    a_sum,count3=0,0
    while temp1 > 0:
        temp1 //= 10
        count3 += 1
    while temp2 > 0:
        rem = temp2 % 10
        a_sum += (rem ** count3)
        temp2 //= 10
    return n1 == a_sum
def numbers():
    n1 = int(input("Enter the starting number: "))
    n2 = int(input("Enter the ending number: "))
    count1 = count2 = count3 = count4 = count5 = count6 = 0
    for i in range(n1, n2 + 1):
        if i > 0:
            if is_prime(i):count1 += 1
            if is_perfect(i):count2 += 1
            if is_armstrong(i):count3 += 1
            if is_prime(i) and is_perfect(i):count4 += 1
            if is_perfect(i) and is_armstrong(i):count5 += 1
            if is_armstrong(i) and is_prime(i):count6 += 1
    print("Prime count:", count1)
    print("Perfect count:", count2)
    print("Armstrong count:", count3)
    print("Prime + Perfect:", count4)
    print("Perfect + Armstrong:", count5)
    print("Armstrong + Prime:", count6)
def math_club():
    n=int(input("Enter how many terms you want: "))
    x=11
    for i in range(n):
        y=x+1
        result = x * y
        if i==n-1:print(result, end="....")
        else:print(result, end=", ")
        x+=1
def cubic_sequence():
    n=int(input("Enter how many cubic numbers you want: "))
    k=1
    print(k,end=',')
    for i in range(1, n):
        answer=i**3+1
        if i==n-1:print(answer,end="....")
        else:print(answer,end=',')
while True:
    print("\n**********************")
    print("1:Prime,Perfect,Armstrong\n2:Multiplication series\n3:Cubic form\n4:Exit")
    print("**********************")
    choice = int(input("Enter your choice: "))
    if choice == 1:numbers()
    elif choice == 2: math_club()
    elif choice == 3:cubic_sequence()
    elif choice == 4:break
    else:print("Invalid choice. Try again.")