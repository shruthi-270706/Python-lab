name=str(input("Enter Full name: "))
weight=int(input("Enter the weight in kilograms: "))
workout_min=int(input("Enter how long did you run for(in minutes): "))
total_calories=workout_min*9.0
estimate_weight_loss=total_calories/7700
print("User full name: ",name)
print("User weight: ",weight)
print("Total calories: ",total_calories)
print(estimate_weight_loss)