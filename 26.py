a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b > c and a + c > b and b + c > a:
    print("The sides form a triangle.")
    if a == b or b == c or a == c: print("The triangle is isosceles.")
    else:print("The triangle is not isosceles.")
else:
    print("Not a triangle.")
