def vowel_count(string):
    count=0
    vowels="AEIOUaeiou"
    for char in string:
        if char in vowels: count+=1
    return count