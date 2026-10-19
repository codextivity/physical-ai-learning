
import math

# Link lengths (meters)
L1 = 4.0
L2 = 3.0

# Target position (meters)


x_target = 2.5
y_target = 4.3301270189



# Distance from robot base to target
distance = math.hypot(x_target, y_target)

# Geometric reachability limits
min_reach = abs(L1 - L2)
max_reach = L1 + L2

print(f"Target distance: {distance:.2f} m")
print(f"Minimum reach:   {min_reach:.2f} m")
print(f"Maximum reach:   {max_reach:.2f} m")

if min_reach <= distance <= max_reach:
    print("Target is geometrically reachable")
else:
    print("Target is unreachable")
