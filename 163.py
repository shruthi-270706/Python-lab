num = int(input("Enter the number of cities: "))
l = []
for i in range(num):
    city = input(f"Enter the {i+1} city name: ")
    l.append(city)
t = tuple(l)  
print("Cities:", t)
longest = l[0] 
for city in l:
    if len(city)>=len(longest):
        longest=city
print("Longest city name:", longest)