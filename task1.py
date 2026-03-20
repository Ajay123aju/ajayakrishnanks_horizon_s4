import math

x1 = float(input("Enter origin X coordinate: "))
y1 = float(input("Enter origin Y coordinate: "))
x2 = float(input("Enter destination X coordinate: "))
y2 = float(input("Enter destination Y coordinate: "))


# Part A: Calculate Distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output Results
print(f"\nDistance to destination: {distance:.2f} m")
