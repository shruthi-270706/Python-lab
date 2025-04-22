def longest_word():
    string=str(input("Enter the string: "))
    new_string=string.split(" ")
    longest=""
    for char in new_string:
        if len(char)>len(longest):
            longest=char
    print(longest)
longest_word()