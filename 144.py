my_dict = {}
n = int(input("Enter the number of key-value pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_dict[key] = value  
search = int(input("Enter the value to search: "))
if search in my_dict.values():print(1)
else:print(0)