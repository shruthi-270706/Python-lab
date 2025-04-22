def swap_case(string):
    result = ""
    for char in string:
        if char.isupper():result += char.lower()  
        elif char.islower():result += char.upper()  
        else:result += char  
    return result
string = input("Enter the string: ")
print("Converted string:", swap_case(string))