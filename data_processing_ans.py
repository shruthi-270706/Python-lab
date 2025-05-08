from data_processing import data_cleaning
num=int(input("Enter the number of elements: "))
data = []
for i in range(num):
    n=int(input("Enter the element: "))
    data.append(n)
cleaned_data = data_cleaning.remove_duplicates(data)

print("Cleaned list:", cleaned_data)