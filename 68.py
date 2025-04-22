def valid_aadhar(aadhar, message="Checking"):
    print(aadhar, message)
    if len(aadhar) != 14:
        return "Invalid Aadhaar number (It must have 14 characters, including spaces)"
    aadhar_parts = aadhar.split(" ")
    if len(aadhar_parts) != 3:
        return "Invalid Aadhaar number (It must be in XXXX XXXX XXXX format)"
    for part in aadhar_parts:
        if len(part) != 4 or not part.isdigit():  
            return "Invalid Aadhaar no.(Each part must have exactly 4 digits and contain only no)"
    return "Valid Aadhaar number"
aadhar = input("Enter your Aadhaar number (XXXX XXXX XXXX): ")
print(valid_aadhar(aadhar))