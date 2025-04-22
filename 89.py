def student_info():
    name=str(input("Enter the name: "))
    print(name)
    add_details=input("Enter details(key:value) and seperated by commas:")
    if add_details:
        details=add_details.split(",")
        for part in details:
            key,value=part.split(":")
            print(f"{key.strip()}:{value.strip()}")
    else:print("No more details")
student_info()