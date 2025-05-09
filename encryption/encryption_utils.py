def encrypt(text):
    encrypted = ''
    for char in text:
        encrypted += chr(ord(char) + 1) 
    return encrypted