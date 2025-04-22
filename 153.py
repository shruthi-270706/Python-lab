num=int(input("Enter the number of members: "))
age={}
for i in range(num):
    name=input("Enter the name: ")
    age[name]=int(input("Enter the age: "))
print(age)
print(f"Oldest age: {max(age.values())}")