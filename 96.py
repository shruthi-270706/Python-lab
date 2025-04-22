string=str(input("Enter the string: "))
vowel='AEIOUaeiou'
count=0
length=len(string)
for ch in string:
    if ch in vowel:count+=1
if (length-count)<=2: print("Happiest")
else:print("Just happy")
sum=length-count
print(f"Difference is: {length}-{count}={sum}")