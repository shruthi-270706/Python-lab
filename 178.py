num = int(input("Enter the number of elements: "))
file_name = input("Enter the file name (with .txt): ")
open(file_name, 'w').close()
open("even_numbers.txt", 'w').close()
open("odd_numbers.txt", 'w').close()
for i in range(num):
    n = int(input("Enter the number: "))
    with open(file_name, 'a') as file:
        file.write(f"{n}\n")
    if n % 2 == 0:
        with open("even_numbers.txt", "a") as even:
            even.write(f"{n}\n")
    else:
        with open("odd_numbers.txt", "a") as odd:
            odd.write(f"{n}\n")
print("\nAll Numbers:")
with open(file_name, "r") as file:
    for line in file:print(line.strip())
print("\nEven Numbers:")
with open("even_numbers.txt", "r") as even:
    for line in even:print(line.strip())
print("\nOdd Numbers:")
with open("odd_numbers.txt", "r") as odd:
    for line in odd:print(line.strip())