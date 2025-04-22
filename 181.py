class students:
    def __init__(self, name, roll_no, marks, address):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.address = address  
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Address:", self.address)
s1 = students("Shruthi", 2298, 98.0, "SRU")
print("Student 1 Details:")
s1.display()
s2 = students("Nandini", 2299, 97.7, "Bhoji Reddy")
print("Student 2 Details:")
s2.display() 
s3 = students("Ambika", 2300, 98.7, "City College")
print("Student 3 Details:")
s3.display() 