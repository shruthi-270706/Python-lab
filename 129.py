num1 = int(input("Enter the number of elements: "))
s1 = []
for i in range(num1):
    num = int(input("Enter a number: "))
    s1.append(num)
s2 = set(s1)  
num2 = int(input("Enter the number of elements: "))
s3 = []
for i in range(num2):
    num = int(input("Enter a number: "))
    s3.append(num)
s4 = set(s3)  
num3 = int(input("Enter the number of elements: "))
s5 = []
for i in range(num3):
    num = int(input("Enter a number: "))
    s5.append(num)  
s6 = set(s5)
subtract=s2-(s4-s6)
print("Subtract of sets: ",subtract)