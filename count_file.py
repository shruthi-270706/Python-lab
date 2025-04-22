file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        text = file.read()
    text = text.lower()
    clean_text = ""
    for char in text:
        if char.isalnum() or char.isspace(): 
            clean_text += char
    words = clean_text.split()
    print(f"\nTotal words: {len(words)}")
    word_count = {}
    for word in words:
        if word in word_count:word_count[word] += 1
        else:word_count[word] = 1
    print("\nWord Frequency:")
    for word in (word_count):print(f"{word}: {word_count[word]}")
except FileNotFoundError:print("File not found!")