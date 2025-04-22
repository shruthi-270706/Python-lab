people = {}
n = int(input("Enter number of people: "))
for _ in range(n):
    name = input("Enter person's name: ")
    age = int(input("Enter age: "))
    people[name] = age
youngest = None
second_youngest = None
for age in people.values():
    if youngest is None or age < youngest:
        second_youngest = youngest
        youngest = age
    elif second_youngest is None or age < second_youngest:
        second_youngest = age
if second_youngest is not None:
    for name, age in people.items():
        if age == second_youngest:
            print("Person with the second youngest age:", name)
            break
else:print("No second youngest age available.")