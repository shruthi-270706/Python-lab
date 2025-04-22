import math
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
area = length * breadth
diagonal = math.sqrt(length**2 + breadth**2)  
print(f"Area of the rectangle: {area}")
print(f"Diagonal of the rectangle: {diagonal}")
