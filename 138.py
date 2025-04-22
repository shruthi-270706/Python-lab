d={0:"Zero", 1: "One",2:"Two",4:"Four",5:"Five",
   6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"
   }
num=int(input("Enter the number: "))
l=[]
if num>0:
    while num!=0:
        n=num%10
        l.append(n)
        num//=10
    l.reverse()
    for i in l:print(d[i],end=" ")
else:print("Invalid Input")