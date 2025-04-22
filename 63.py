def char_present():
    name=str(input("Enter your name: "))
    st=str(input("Enter the letter you want to find: "))
    count=0
    for ch in name:
        if (ch==st): count+=1
    if(count>=1):print("It is present")
    else:print("It is not found")
char_present()