import json
name = input("Enter your name: ")
age = int(input("Enter your age: "))
data = {'name': name, 'age': age}
json_string = json.dumps(data)
print("JSON Output:", json_string)