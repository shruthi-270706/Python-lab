students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    students[name] = score
highest = None
second_highest = None
for score in students.values():
    if highest is None or score > highest:
        second_highest = highest
        highest = score
    elif second_highest is None or score > second_highest:
        second_highest = score
if second_highest is not None:
    for name, score in students.items():
        if score == second_highest:
            print("Student with the second highest score:", name)
            break
else:print("No second highest score available.")