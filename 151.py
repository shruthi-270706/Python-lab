import math
def calculate_viewing_angle():
    distance=float(input("Enter the distance from the projector to the screen(in meters): "))
    height = float(input("Enter the height of the screen (in meters): "))
    angle_radians = math.atan(height / distance)
    angle_degrees = math.degrees(angle_radians)
    print(f"The viewing angle is {angle_degrees:.2f} degrees.")
calculate_viewing_angle()