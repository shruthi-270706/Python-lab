name=str(input("Enter your name: "))
word=str(input("Enter your leter: "))
count=0
for char in name:
    if (char==word):count+=1
if(count>0):print(count)
else: print("Your letter is not found" )