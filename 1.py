import math
print("Square Perimeter")
area_square = float(input("Enter the area of the square (S): "))
if area_square < 0:
    print("Error: Area cannot be negative!")
else:
    side_a = math.sqrt(area_square)
    perimeter_square = 4 * side_a
    print(f"Perimeter of the square: {perimeter_square:.2f}")