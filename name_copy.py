source_file = input("Enter the source file name: ")
destination_file=input("Enter the destination file name: ")
try:
    with open(source_file, 'r') as src:
        content = src.read()  
    with open(destination_file, 'w') as dest:
        dest.write(content) 
    print("\nFile copied successfully!")
except FileNotFoundError:
    print("\nOops! The source file was not found.")