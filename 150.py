import math
import random
def calculate_standard_deviation():
    temperatures = [random.randint(-10, 40) for _ in range(30)]
    mean_temp = math.fsum(temperatures) / len(temperatures)
    variance=math.fsum((temp-mean_temp) ** 2 for temp in temperatures) / len(temperatures)
    std_dev = math.sqrt(variance)
    print("Temperature Data:", temperatures)
    print(f"Mean Temperature: {mean_temp:.2f}°C")
    print(f"Standard Deviation: {std_dev:.2f}°C")
    if std_dev < 5:print("The temperature variations are low (stable weather).")
    elif std_dev < 10:print("The temperature variations are moderate.")
    else:print("The temperature variations are high (unstable weather).")
calculate_standard_deviation()