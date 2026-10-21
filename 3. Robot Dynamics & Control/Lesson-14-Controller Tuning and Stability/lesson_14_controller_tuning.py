
import numpy as np
import matplotlib.pyplot as plt

I = 0.5
b = 0.2
m, L, g = 1.0, 0.5, 9.81

target = np.deg2rad(45)
dt = 0.005
duration = 3.0
steps = int(duration / dt)

controllers = {
    "Underdamped": (12.0, 0.3),
    "Near-critical": (12.0, 4.7),
    "Overdamped": (12.0, 10.0),
}

def simulate(Kp, Kd):
    theta, omega = 0.0, 0.0
    angles = [0.0]

    for _ in range(steps):
        error = target - theta

        torque = (
            Kp * error
            - Kd * omega
            + m * g * L * np.cos(theta)
        )

        alpha = (
            torque
            - b * omega
            - m * g * L * np.cos(theta)
        ) / I

        omega += alpha * dt
        theta += omega * dt
        angles.append(np.rad2deg(theta))

    return np.array(angles)

time = np.linspace(0, duration, steps + 1)

for name, (Kp, Kd) in controllers.items():
    angles = simulate(Kp, Kd)

    zeta = (b + Kd) / (2 * np.sqrt(I * Kp))
    overshoot = max(0.0, np.max(angles) - 45.0)
    final_error = abs(45.0 - angles[-1])

    print(f"\n{name}")
    print(f"  Kp = {Kp}, Kd = {Kd}")
    print(f"  Damping ratio = {zeta:.3f}")
    print(f"  Overshoot = {overshoot:.3f} degrees")
    print(f"  Final error = {final_error:.3f} degrees")

    plt.plot(time, angles, label=f"{name} (zeta={zeta:.2f})")

plt.axhline(45, linestyle="--", label="Target")
plt.xlabel("Time (s)")
plt.ylabel("Joint angle (degrees)")
plt.title("Lesson 14: PD Controller Tuning")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("lesson_14_controller_tuning.png", dpi=160)
plt.show()
