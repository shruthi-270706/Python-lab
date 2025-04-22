name=input("Enter the name of the user: ")
weight=int(input("Enter the weight (in kg)"))
running=int(input("Enter the number of minutes: "))
calories=running*9.0
weightloss=calories/7700
print("----FITNESS TRACKER RESULTS----")
print("Full name: ",name)
print(f"Weight: {weight} kg")
print(f"Duration of running: {running} minutes")
print("Calories Burned per minute: 9.00")
print(f"Total calories burned: {calories}calories")
print(f"Estimated weight loss: {weightloss:.4f}kg")