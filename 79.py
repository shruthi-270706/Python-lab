def weather(current_temp,condition):
    print("The Current Temperature is:",current_temp)
    print("The Current Condition is:",condition)
    if(current_temp>=25):
        print("Its sunny Today!! Wear light clothes and sunglasses")
    else:
        print("Its rainy Today!! Wear a warm jacket and carry an Umbrella")
current_temp=float(input("Enter the temperature( in celusis): "))
condition=str(input("Enter the weather condition: "))
weather(current_temp,condition)