num = int(input("Enter the number of elements: "))  
t1 = []    
for i in range(num):  
    element = int(input("Enter the element: "))  
    t1.append(element) 
t1 = tuple(t1)   
print("Tuple:", t1)
c1=t1.count(int(input("Enter the no. u want to count: ")))
print(c1)