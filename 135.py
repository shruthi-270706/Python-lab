def sets():
    num1 = int(input("Enter the number of elements in set1: "))
    s1 = []
    for i in range(num1):
        ele1 = int(input("Enter the number: "))
        s1.append(ele1)
    s2 = set(s1)
    print(s2)
sets()