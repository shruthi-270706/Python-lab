file_name=input("Enter the file name (with .txt): ")
message=input("Enter the message to append into it: ")
with open(file_name,"a") as file:
    file.write(message+"\n")
print(f"Your message is saved in {file_name}")