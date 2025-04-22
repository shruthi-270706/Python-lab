num=int(input("Enter the no.of drugs u want to enter: "))  
t1 = []  
for i in range(num):  
    drug_name = input("Enter the Drug name: ")  
    drug_formula = input("Enter the Drug formula: ")  
    drug_brand = input("Enter the Drug Brand: ")  
    drug_mrp = int(input("Enter the Drug MRP: "))  
    drug_mfg = input("Enter the Drug MFG Date: ")  
    drug_expiry = input("Enter the Drug Expiry Date: ")  
    drug_quantity = int(input("Enter the Drug Quantity: "))  
    t1.append((drug_name,drug_formula,drug_brand,drug_mrp,drug_mfg,drug_expiry,drug_quantity))
perfect_tuple = tuple(t1)  
print("\nFinal Ordered Tuple:")
print(perfect_tuple)
while True:
    print("Enter 1:MRP in increasing order: ")
    print("Enter 2:list out expiry date: ")
    print("Enter 3:Remove expired date drugs from the list")
    print("Enter 4:Print count of each type of drug: ")
    print("Enter 5:Diplay all drugs with all details" )
    choice=int(input("Enter your choice: "))
    if choice==1: