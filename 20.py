num=int(input("Enter the number: "))
decimal,i=0,0
while num>0:
    r=num%10
    exp=r*(2**i)
    decimal=decimal+exp
    num=num//10
    i+=1
print("Decimal number:",decimal)