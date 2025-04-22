def vowel():
    name=str(input("Enter the name: "))
    count=0
    vowel='aeiou'
    string_parts=name.split("$")
    print(string_parts)
    for ch in name:
        if ch in vowel: count+=1
    print(count)
vowel()