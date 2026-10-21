
import numpy as np
import matplotlib.pyplot as plt

mass = 2.0       # kg
length = 0.5     # m
gravity = 9.81   # m/s^2

angles_deg = np.linspace(0, 90, 181)
angles_rad = np.deg2rad(angles_deg)

# Gravitational torque magnitude for a point-mass payload
torque = mass * gravity * length * np.cos(angles_rad)

print("Gravity torque experiment")
for angle in [0, 30, 60, 90]:
    value = mass * gravity * length * np.cos(np.deg2rad(angle))
    print(f"Angle {angle:2d} deg: {value:.3f} N·m")

assert np.isclose(torque[0], 9.81)
assert np.isclose(torque[-1], 0.0, atol=1e-10)

print("Verification: PASSED")

plt.figure(figsize=(8, 5))
plt.plot(angles_deg, torque)
plt.xlabel("Arm angle from horizontal (degrees)")
plt.ylabel("Gravity torque magnitude (N·m)")
plt.title("Lesson 11: Payload Gravity Torque")
plt.grid(True)
plt.savefig("lesson_11_gravity_torque.png", dpi=160)
plt.show()
