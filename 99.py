string = input("Enter the string: ")
vowel = 'AEIOUaeiou'
result = " "
index=0
while index<len(string):
    ch=string[index]
    if ch not in vowel:
        result+=ch
    index+=1
print(result)