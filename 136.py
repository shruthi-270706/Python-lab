num=int(input("Enter the no.of Drugs: "))
t1=[]
for i in range(num):
    drug_name=input("Enter the Drug name: ")
    drug_formula=input("Enter the Drug formula: ")
    drug_brand=input("Enter the Drug brand: ")
    drug_mrp=int(input("Enter the Drug MRP: "))
    drug_mfg=input("Enter the Drug Mfg(DD-MM-YYYY): ")
    drug_expiry=input("Enter the Drug expiry(YYYY-MM-DD): " )
    drug_quantity=int(input("Enter the Drug quantity: "))
    t1.append((drug_name,drug_formula,drug_brand,drug_mrp,drug_mfg,drug_expiry,drug_quantity))
t2=tuple(t1)
print(t2)
while True:
    print("\n1:Increasing MRP\n2:List of Expiry Date\n3:Delete Expiry Date")
    print("4:Count no.of Drugs\n5:Details of Each")
    choice=input("Enter your choice: ")
    if choice=="1":
        for i in range(len(t1)):
            for j in range(len(t1)-i-1):
                if t1[j][3]>t1[j+1][3]:
                    t1[j],t1[j+1]=t1[j+1],t1[j]
        new_tuple=tuple(t1)
        for drug in new_tuple:print(drug)
    elif choice=="2":
        present_date=input("Enter the present date(YYYY-MM-DD): ")
        for drug in t1:
            expiry_date=drug[5]
            if expiry_date<present_date:
                print(f"{drug[0]}:{drug[5]} (Expired)")
    elif choice=="3":
        present_date=input("Enter the present date(YYYY-MM-DD): ")
        i=0
        while i<len(t1):
            expiry_date=t1[i][5]
            if expiry_date<present_date:t1.remove(t1[i])
            else:i+=1
        print(t1)
    elif choice=="4":
        print(len(t1))
    elif choice=="5":
        for j in t2:print(j)
    else: break
