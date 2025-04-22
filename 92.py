def lowercase():
    string=str(input("Enter the string: "))
    c1,c2,c3,c4,c5=0,0,0,0,0
    for ch in string:
        if (ch=='a'):c1+=1
        elif(ch=='e'):c2+=1
        elif(ch=='i'):c3+=1
        elif(ch=='o'):c4+=1
        elif(ch=='u'):c5+=1    
    print(f"a :{c1}")
    print(f"e :{c2}")
    print(f"i :{c3}")
    print(f"o :{c4}")
    print(f"u :{c5}")
lowercase()