num = int(input("Enter the number of elements: "))
s1 = []
for i in range(num):
    n = int(input("Enter the number: "))  
    s1.append(n)
s2 = set(s1)
print("The given set: ", s2)
s2.add(int(input("Enter the adding number: ")))  
print("The modified set: ", s2)
s2.discard(2)  
print("Element is removed: ", s2)
print("Is the set empty?", len(s2) == 0)
s2.pop()
print(s2)
s2.clear()
print("Set after clearing:", s2)