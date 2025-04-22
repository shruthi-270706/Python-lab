def sub_string(s, sub):
    count = 0
    sub_len = len(sub)  
    for i in range(len(s) - sub_len + 1): 
        if s[i:i + sub_len] == sub:  
            count += 1
    print(count)
s = input("Enter the string: ")
sub = input("Enter the substring: ")
sub_string(s, sub)