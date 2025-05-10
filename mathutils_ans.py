from mathutils import arthmetics as ar
from mathutils import geometry as gm
def arthmetic_fun():
    num1=int(input("Enter the number1: "))
    num2=int(input("Enter the number2: "))
    add_ans=ar.add(num1,num2)
    sub_ans=ar.sub(num1,num2)
    mul_ans=ar.mul(num1,num2)
    div_ans=ar.div(num1,num2)
    print(add_ans)
    print(sub_ans)
    print(mul_ans)
    print(div_ans)
def geometry_fun():
    print("1:Circle radius\n2:Rectangle Area\n3:Rectangle Perimeter")
    choice1=int(input("Enter your choice: "))
    if choice1==1:
        radius=int(input("Enter the radius: "))
        circle_radius=gm.circle(radius)
        print(circle_radius)
    elif choice1==2:
        length=int(input("Enter the length of rectangle: "))
        breadth=int(input("Enter the breadth of rectangle: "))
        rectanglearea_ans=gm.rectangle_area(length,breadth)
        print(rectanglearea_ans)
    elif choice1==3:
        length=int(input("Enter the length of rectangle: "))
        breadth=int(input("Enter the breadth of rectangle: "))
        rectangleperi_ans=gm.rectangle_perimter(length,breadth)
        print(rectangleperi_ans)
print("1:Arthmetic \n2:Geometry" )
choice=int(input("Enter your choice: "))
if choice==1:arthmetic_fun()
elif choice==2: geometry_fun()