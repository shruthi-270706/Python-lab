name = str(input("Enter your name: ")) 
count=0
name=name.lower()
for char in name:
    if char in 'aeiou':
        count+=1
print(count)