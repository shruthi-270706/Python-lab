def armstrong():
    number=int(input("Enter the number: "))
    count=sum=0
    temp1=temp2=number
    while (temp1>0):
        temp1//=10
        count+=1
    while (temp2>0):
        rem=temp2%10
        sum+=(rem**count)
        temp2//=10
    return sum==number
print(armstrong())