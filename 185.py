class student:
    def __init__(self, name, roll_no, marks, address):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.address = address
    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.marks)
        print(self.address)
s1 = student("Pramod", 1217, 87.9, "SRU")
print("Student1 Details are :")
s1.display()
s2 = student("Mahesh", 3456, 56.9, "SRIIT, Hyd")
print("Student2 Details are :")
s2.display()
s3 = student("Samanya", 7894, 66.9, "SRIT, HNK")
print("Student3 Details are :")
s3.display()