name = input("Enter a string: ")
count = 0
words = name.split(" ")
for word in words:
    word_count=0
    for char in word:
        if char in 'aeiouAEIOU':  
            word_count += 1
    if word_count > 0:
        print(f"Word '{word}' has {word_count} vowels")
        count += word_count  
print(f"Total vowels in the entire string: {count}")
