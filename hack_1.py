def analyze_rainfall(rainfall):
    if len(rainfall)!=7:
        print("Exactly 7 days of data required.")
        return
    for r in rainfall:
        if r<0:
            print("Rainfall cannot be negative.")
            return
    total=sum(rainfall)
    average=total / 7
    max_rain=max(rainfall)
    max_days=[]
    for i in range(7):
        if rainfall[i]==max_rain:
            max_days.append(i + 1)
    below_avg = 0
    for r in rainfall:
        if r<average:
            below_avg+=1
    print("Total rainfall:", total, "mm")
    print("Average rainfall:", round(average, 2), "mm")
    print("Day(s) with maximum rainfall:", max_days)
    print("Days with rainfall below average:", below_avg)
rain = []
print("Enter Rain in mm for 7 Days: ")
for i in range(7):
    n = int(input(f"Day {i+1}: "))
    rain.append(n)
analyze_rainfall(rain)