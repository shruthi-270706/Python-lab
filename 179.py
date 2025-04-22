file_name = input("Enter the file name (with .txt): ")
print("Enter your paragraph (type END to stop):")
paragraph = ""
while True:
    line = input()
    if line == "END":
        break
    paragraph += line + "\n"
with open(file_name, 'w') as f:
    f.write(paragraph)
vowels = 'AEIOUaeiou'
lower=,upper,digit,space,newline,vowel_count,special= 0
with open(file_name, 'r') as f:
    data = f.read()
    for ch in data:
        if ch in vowels:vowel_count += 1
        if ch.islower():lower += 1
        elif ch.isupper():upper += 1
        elif ch.isdigit():digit += 1
        elif ch == ' ' or ch == '\t':space += 1
        elif ch == '\n':newline += 1
        elif not ch.isalnum() and ch not in [' ', '\n', '\t']:special += 1
print("Lowercase letters:", lower)
print("Uppercase letters:", upper)
print("Digits:", digit)
print("Spaces and tabs:", space)
print("Newlines:", newline)
print("Vowels:", vowel_count)
print("Special characters:", special)
with open(file_name, 'a') as f:
    f.write("\n\n--- Summary ---\n")
    f.write("Lowercase letters: " + str(lower) + "\n")
    f.write("Uppercase letters: " + str(upper) + "\n")
    f.write("Digits: " + str(digit) + "\n")
    f.write("Spaces and tabs: " + str(space) + "\n")
    f.write("Newlines: " + str(newline) + "\n")
    f.write("Vowels: " + str(vowel_count) + "\n")
    f.write("Special characters: " + str(special) + "\n")