m1=int(input("Enter the marks of subject 1: "))
m2=int(input("Enter the marks of subject 2: "))
m3=int(input("Enter the marks of subject 3: "))
m4=int(input("Enter the marks of subject 4: "))
m5=int(input("Enter the marks of subject 5: "))
m6=int(input("Enter the marks of subject 6: "))
average=(m1+m2+m3+m4+m5+m6)/6
if (average > 90): print("A")
elif (average >80 and average < 90): print("B")
elif (average >70 and average <80): print("C")
elif (average >60 and average <70): print("D")
elif (average <60): print("FAIL")