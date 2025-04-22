num = int(input("Enter the number of students: "))
students = {}
for i in range(num):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    students[name] = marks
print(students)
first = second = third = float("-inf")
for score in students.values():
    if score > first:
        third = second
        second = first
        first = score
    elif score > second and score != first:
        third = second
        second = score
    elif score > third and score != first and score != second:
        third = score
for name, score in students.items():
    if score == third:
        print(f"{name}:{third}")
        break