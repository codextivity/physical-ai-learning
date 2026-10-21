
import numpy as np
import matplotlib.pyplot as plt

# Robot dynamics
I = 0.5
b = 0.2
m, L, g = 1.0, 0.5, 9.81

# PD controller
Kp = 12.0
Kd = 3.0

target = np.deg2rad(90.0)
dt = 0.005
duration = 4.0
steps = int(duration / dt)

def simulate(torque_limit):
    theta, omega = 0.0, 0.0
    angles = [0.0]
    saturated_steps = 0

    for _ in range(steps):
        error = target - theta

        requested = (
            Kp * error
            - Kd * omega
            + m*g*L*np.cos(theta)
        )

        applied = np.clip(
            requested, -torque_limit, torque_limit
        )

        if abs(requested) > torque_limit:
            saturated_steps += 1

        alpha = (
            applied - b*omega
            - m*g*L*np.cos(theta)
        ) / I

        omega += alpha*dt
        theta += omega*dt

        angles.append(np.rad2deg(theta))

    return np.array(angles), saturated_steps

# Compare unconstrained and torque-limited motors
unlimited, _ = simulate(float("inf"))
limited, saturated = simulate(5.0)

time = np.linspace(0, duration, steps + 1)

print(f"Unlimited final angle: {unlimited[-1]:.3f} deg")
print(f"Limited final angle:   {limited[-1]:.3f} deg")
print(f"Saturated time steps:  {saturated}")

assert saturated > 0
assert np.all(np.isfinite(limited))
print("Verification: PASSED")

plt.plot(time, unlimited, label="Unlimited motor")
plt.plot(time, limited, label="Torque limit: 5 N·m")
plt.axhline(90, linestyle="--", label="Target")
plt.xlabel("Time (s)")
plt.ylabel("Joint angle (degrees)")
plt.title("Lesson 15: Actuator Torque Saturation")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("lesson_15_torque_saturation.png", dpi=160)
plt.show()
