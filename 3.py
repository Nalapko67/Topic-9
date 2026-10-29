import math
print("Right-Angled Triangle")
leg_a = float(input("Enter the first leg (a): "))
leg_b = float(input("Enter the second leg (b): "))
if leg_a <= 0 or leg_b <= 0:
    print("Analysis: Triangle does not exist (legs must be > 0).")
else:
    print("Analysis: Right-angled triangle exists.")
    hypotenuse = math.sqrt(leg_a**2 + leg_b**2)
    triangle_perimeter = leg_a + leg_b + hypotenuse
    print(f"Hypotenuse: {hypotenuse:.2f}")
    print(f"Triangle perimeter: {triangle_perimeter:.2f}")