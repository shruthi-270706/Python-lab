from encryption import encryption_utils
text = input("Enter the word: ")
result = encryption_utils.encrypt(text)
print("Encrypted string:", result)