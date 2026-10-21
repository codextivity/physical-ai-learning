
import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
I = 0.5
b = 0.2
m = 1.0
L = 0.5
g = 9.81

# Controller gains
Kp = 12.0
Kd = 3.0

# Target and initial state
target = np.deg2rad(45.0)
theta = 0.0
omega = 0.0

dt = 0.005
duration = 3.0
steps = int(duration / dt)

time_log = []
angle_log = []
torque_log = []

for step in range(steps):
    time = step * dt

    # Feedback control
    error = target - theta
    gravity_comp = m * g * L * np.cos(theta)

    motor_torque = (
        Kp * error
        - Kd * omega
        + gravity_comp
    )

    # Robot dynamics
    alpha = (
        motor_torque
        - b * omega
        - m * g * L * np.cos(theta)
    ) / I

    # Semi-implicit Euler integration
    omega += alpha * dt
    theta += omega * dt

    time_log.append(time)
    angle_log.append(np.rad2deg(theta))
    torque_log.append(motor_torque)

final_angle = np.rad2deg(theta)
final_error = abs(45.0 - final_angle)

print(f"Target angle: 45.00 degrees")
print(f"Final angle: {final_angle:.3f} degrees")
print(f"Final error: {final_error:.4f} degrees")

passed = final_error < 1.0
print("Verification: PASSED" if passed else "Verification: FAILED")

plt.figure(figsize=(8, 5))
plt.plot(time_log, angle_log, label="Joint angle")
plt.axhline(45.0, linestyle="--", label="Target 45 deg")
plt.xlabel("Time (seconds)")
plt.ylabel("Joint angle (degrees)")
plt.title("Lesson 13: PD Joint Position Control")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("lesson_13_pd_response.png", dpi=160)
plt.show()
