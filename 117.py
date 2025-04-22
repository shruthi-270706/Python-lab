num = int(input("Enter the number of elements: "))  
t1 = []   
for i in range(num):  
    element = int(input("Enter the element: "))  
    t1.append(element) 
t1 = tuple(t1)  
print("Tuple:", t1)   
search = int(input("Enter the element you want to search: "))  
if search in t1:  print("True")  
else:  print("False")  