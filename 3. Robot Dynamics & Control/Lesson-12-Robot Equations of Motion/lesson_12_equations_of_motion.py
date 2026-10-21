
import numpy as np
import matplotlib.pyplot as plt

# Simplified single-joint robot
I = 0.5       # kg*m^2
b = 0.2       # N*m*s/rad
m = 1.0       # kg
L = 0.5       # m
g = 9.81      # m/s^2

dt = 0.005
duration = 1.0
steps = int(duration / dt)

def simulate(motor_torque):
    theta = 0.0     # Horizontal starting pose
    omega = 0.0     # Initially at rest

    angles = [theta]

    for _ in range(steps):
        gravity_torque = m * g * L * np.cos(theta)

        alpha = (
            motor_torque
            - b * omega
            - gravity_torque
        ) / I

        # Semi-implicit Euler integration
        omega += alpha * dt
        theta += omega * dt

        angles.append(theta)

    return np.rad2deg(np.array(angles))

# Case A: motor supplies no torque
without_motor = simulate(0.0)

# Case B: motor balances gravity at horizontal
holding_torque = m * g * L
with_motor = simulate(holding_torque)

time = np.linspace(0, duration, steps + 1)

print(f"Holding torque: {holding_torque:.3f} N*m")
print(f"No motor final angle: {without_motor[-1]:.2f} deg")
print(f"Holding motor final angle: {with_motor[-1]:.2f} deg")

assert without_motor[-1] < -1.0
assert np.allclose(with_motor, 0.0, atol=1e-8)
print("Verification: PASSED")

plt.plot(time, without_motor, label="No motor torque")
plt.plot(time, with_motor, label="Gravity compensation")
plt.xlabel("Time (s)")
plt.ylabel("Joint angle (degrees)")
plt.title("Lesson 12: Single-Joint Dynamics")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("lesson_12_joint_dynamics.png", dpi=160)
plt.show()
