def vowel_count(s):
    count=0
    vowel="AEIOUaeiou"
    for ch in s:
        if ch in vowel:count+=1
    return "The Total count of vowels in the string are: ",count
s=str(input("Enter the string: "))
print(vowel_count(s))