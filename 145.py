library={}
num=int(input("Enter the number of key-values stocks: "))
for i in range(num):
    key=input("Enter ID of stock: ")
    name=input("Enter the name: ")
    price=int(input("Enter the price: "))
    quantity=int(input("Enter the quantity: "))
    library[key]=[name,price,quantity]
print(library)
def add():
    key=input("Enter ID of stock: ")
    if key in library:print(f"{key} is already in Stocks")
    else:
        name=input("Enter the name: ")
        price=int(input("Enter the price: "))
        quantity=int(input("Enter the quantity: "))
        library[key]=[name,price,quantity]
        print(f"{key} is added to stock")
def update():
    key=input("Enter ID of stock: ")
    if key in library:
        quantity=int(input("Enter the updated quantity:" ))
        l=library[key]
        l[2]=quantity
        library[key]=l
        print(library[key])
        print(f"{key} is updated with {quantity}")
    else:print(f"{key} is not found in Stocks")
def search():
    search=input("Enter ID you want to search: ")
    if search in library.keys():
        print(f"{search} is present in stock")
    else:print(f"{search} is not in stocks")
def calculate():
    key=input("Enter ID of stock: ")
    if key in library:
        l1=library[key]
        calculate1=l1[2]*l1[1]
        print(f"{key} total of {calculate1}")
    else:print(f"{key} is not in stocks")
def end_program():
    print("exit")
    exit()
while True:
    print("1:Add\n2:Update\n3:Search\n4:Calculate\n5:Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:add()
    elif choice==2:update()
    elif choice==3:search()
    elif choice==4:calculate()
    elif choice==5:end_program()