a=int(input("Enter the amount of first item: "))
b=int(input("Enter the amount of second item: "))
c=int(input("Enter the amount of third item: "))
subtotal=a+b+c
gst=(subtotal*(20/100))
final_amount=subtotal+gst
print(f"Subtotal of items are: {subtotal}")
print(f"Gst: {gst}")
print(f"Final amount: {final_amount}")