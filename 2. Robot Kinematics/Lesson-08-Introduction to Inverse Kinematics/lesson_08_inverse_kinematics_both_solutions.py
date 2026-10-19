
import math

# Robot geometry (meters)
L1 = 4.0
L2 = 3.0

# Target position (meters)





x_target = 2.5
y_target = 4.3301270189







# Check geometric reachability before IK
distance = math.hypot(x_target, y_target)

min_reach = abs(L1 - L2)
max_reach = L1 + L2

print(f"Target distance: {distance:.3f} m")
print(f"Reachable range: {min_reach:.3f} to {max_reach:.3f} m")

if not (min_reach <= distance <= max_reach):
    raise SystemExit("IK stopped: Target is geometrically unreachable")


# Step 1: Calculate cos(theta2)
cos_theta2 = (
    x_target**2 + y_target**2 - L1**2 - L2**2
) / (2 * L1 * L2)

# Step 2: Calculate elbow angle (positive branch)
# theta2 = math.acos(cos_theta2)

theta2 = math.acos(cos_theta2)


theta2_negative = -math.acos(cos_theta2)
print(f"Negative elbow angle: {math.degrees(theta2_negative):.2f} degrees")


beta_negative = math.atan2(L2 * math.sin(theta2_negative), L1 + L2 * math.cos(theta2_negative))
print(f"Negative-elbow beta: {math.degrees(beta_negative):.2f} degrees")


# Step 3: Calculate shoulder angle
alpha = math.atan2(y_target, x_target)


theta1_negative = alpha - beta_negative
print(f"Negative-elbow shoulder: {math.degrees(theta1_negative):.2f} degrees")


x_fk_negative = L1 * math.cos(theta1_negative) + L2 * math.cos(theta1_negative + theta2_negative)
print(f"Negative-elbow FK X: {x_fk_negative:.6f} m")



y_fk_negative = L1 * math.sin(theta1_negative) + L2 * math.sin(theta1_negative + theta2_negative)
print(f"Negative-elbow FK Y: {y_fk_negative:.6f} m")



error_x_negative = x_fk_negative - x_target
print(f"Negative-elbow X error: {error_x_negative:.12e} m")


# Verify Solution B with the same numerical tolerance as Solution A
error_x_negative = x_fk_negative - x_target
error_y_negative = y_fk_negative - y_target

tolerance = 1e-6

print("\n--- Solution B Verification ---")
print(f"X error: {error_x_negative:.12e} m")
print(f"Y error: {error_y_negative:.12e} m")

negative_pass = (
    abs(error_x_negative) < tolerance
    and abs(error_y_negative) < tolerance
)

print("Solution B: PASSED" if negative_pass else "Solution B: FAILED")


beta = math.atan2(
    L2 * math.sin(theta2),
    L1 + L2 * math.cos(theta2)
)

theta1 = alpha - beta

# Convert angles to degrees for display
theta1_deg = math.degrees(theta1)
theta2_deg = math.degrees(theta2)

print(f"Shoulder angle: {theta1_deg:.2f} degrees")
print(f"Elbow angle:    {theta2_deg:.2f} degrees")


# Step 4: Verify IK using forward kinematics
x_fk = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
y_fk = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)

# Step 5: Compare with the target
error_x = x_fk - x_target
error_y = y_fk - y_target

print()
print("Forward Kinematics Verification")
print(f"Target X:   {x_target:.6f} m")
print(f"FK X:       {x_fk:.6f} m")
print(f"Target Y:   {y_target:.6f} m")
print(f"FK Y:       {y_fk:.6f} m")
print(f"X error:    {error_x:.6f} m")
print(f"Y error:    {error_y:.6f} m")

print(f"X error (scientific): {error_x:.12e} m")
print(f"Y error (scientific): {error_y:.12e} m")

