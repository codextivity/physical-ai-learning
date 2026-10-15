
import math

# Link lengths in meters
L1 = 3.0
L2 = 2.0

# Joint angles in degrees
theta1_deg = 0.0
theta2_deg = 60.0

# Python's math.sin and math.cos expect radians
theta1 = math.radians(theta1_deg)
theta2 = math.radians(theta2_deg)

# Forward kinematics
x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)

print(f"Gripper X: {x:.3f} m")
print(f"Gripper Y: {y:.3f} m")
