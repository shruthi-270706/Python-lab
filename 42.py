age=int(input("Enter the age of the person"))
ticket_price=250
if(age<12): discount=80
elif(12<age<=18):discount=30
elif(19<age<=59):discount=0
else: discount=50
total=ticket_price-(ticket_price*discount/100)
print("Your ticket price is:",total)