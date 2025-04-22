num = int(input("Enter the number of elements: "))  
t1 = []    
for i in range(num):  
    element = int(input("Enter the element: "))  
    t1.append(element) 
t1 = tuple(t1)   
print("Tuple:", t1)   
search = int(input("Enter the element you want to search: "))  
if search in t1:
    for i in range(len(t1)):
        if t1[i]==search:
            print(f"Element is present at {i}")
            break
else:  
    t1 = t1 + (search,)  
    print(f"Element not found. Updated tuple: {t1}")  