file_name=input("Enter the file name: ")
try:
    with open(file_name,'r') as file:
        print("\n****FILE CONTENT****")
        print(file.read())
except FileNotFoundError:print("File not found!! A new File will be created")
message=input("Enter the message into the file: ")
with open (file_name,'a') as file:
    file.write(message)
print("Finish")