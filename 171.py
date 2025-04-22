import re
text = input("Enter the text: ")
pattern = 'o'
matches = re.findall(pattern, text)
print(matches)