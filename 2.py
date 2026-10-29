import math
print("Ring Area")
outer_radius = float(input("Enter the outer radius (R): "))
inner_radius = float(input("Enter the inner radius (r): "))
if outer_radius <= 0 or inner_radius <= 0:
    print("Error: Radii must be positive numbers!")
elif inner_radius >= outer_radius:
    print("Error: Inner radius must be less than outer radius (r < R)!")
else:
    ring_area = math.pi * (outer_radius**2 - inner_radius**2)
    print(f"Area of the ring: {ring_area:.2f}")