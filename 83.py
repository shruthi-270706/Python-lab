def vowel_count(s):
    result=""
    for char in s:
        if char not in result:result+=char
    return result
s=str(input("Enter the string: "))
print(vowel_count(s))