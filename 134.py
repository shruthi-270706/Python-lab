set1=input("Enter the elements: ")
new_set=set1.split()
remove_element=input("Enter the element you want to remove: ")
new_set.remove(remove_element)
new_one=set(new_set)
print(new_one)