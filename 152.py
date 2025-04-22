num = int(input("Enter the number of cities: "))
l = []
for i in range(num):
    city = input(f"Enter the {i+1} city name: ")
    l.append(city)
t = tuple(l)  
print("Cities:", t)
shortest = l[0] 
for city in l:
    if len(city)<=len(shortest):
        shortest=city
print("Shortest city name:", shortest)