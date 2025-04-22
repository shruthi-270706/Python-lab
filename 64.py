def vowel():
    name=str(input("Enter the name: "))
    vowel='aeiou'
    sum=0
    string_parts=name.split("$")
    print(string_parts)
    for part in string_parts:
        count=0
        for ch in part:
            if ch in vowel:count+=1
        print(count)
        sum+=count
    print("Total count",sum)
vowel() 