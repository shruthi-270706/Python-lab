sum=0
while True:
    num=int(input("Enter the number: "))
    sum+=num
    if(sum>100):
        break
print("Your sum exceeded 100!!,final answer is",sum)