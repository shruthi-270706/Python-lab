secret_number=int(input("Enter the secret number: "))
user_number=int(input("Enter your number: "))
while True:
    if(secret_number==user_number):
        print("You got the correct number ")
        break
    elif(user_number>=50):
        print("Your number is too high ")
    else:
        print("Your number is too low ")
    user_number=int(input("Try again"))