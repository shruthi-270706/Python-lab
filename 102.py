def find_number():
    elements=input("Enter the elements by giving space: ")
    print(elements)
    found=0
    new_string=elements.split()
    for i in range(len(new_string)):
        if new_string[i].isdigit():
            print(f"Number is at index{i}")
            found+=1
    if (found==0):print("There are no digits in the list")
find_number()