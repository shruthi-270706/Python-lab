def hates():
    name = input("Enter the string: ")
    result = ""
    for ch in name:
        if ch == 'y':
            break
        result += ch  
    print(result)  
hates()