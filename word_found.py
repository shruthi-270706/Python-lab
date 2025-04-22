file_name=input("Enter the file name (with .txt): ")
message=input("Enter the word to search: ")
try:
    with open(file_name,'r') as file:
        line_no=1
        found=False
        for lines in file:
            if message in lines:
                print(f"Word is found at {line_no}")
                found=True
            line_no+=1
        if not found:print("It is not found")
except FileNotFoundError: print(f"No file with {file_name}")