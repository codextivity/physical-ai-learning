
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

true_distance = 2.0
noise_std = 0.10
num_samples = 100

# Simulated sensor readings
measurements = (
    true_distance
    + rng.normal(0, noise_std, num_samples)
)

# Cumulative average
running_average = np.cumsum(measurements) / np.arange(
    1, num_samples + 1
)

single_error = abs(measurements[0] - true_distance)
average_error = abs(running_average[-1] - true_distance)

print(f"True distance: {true_distance:.3f} m")
print(f"First reading: {measurements[0]:.3f} m")
print(f"Average reading: {running_average[-1]:.3f} m")
print(f"First-reading error: {single_error:.4f} m")
print(f"Average error: {average_error:.4f} m")

assert len(measurements) == num_samples
assert np.isfinite(running_average).all()
assert average_error < 0.05
print("Verification: PASSED")

plt.figure(figsize=(9, 5))
plt.plot(measurements, ".", alpha=0.4, label="Noisy readings")
plt.plot(running_average, label="Running average")
plt.axhline(true_distance, linestyle="--", label="True distance")
plt.xlabel("Measurement number")
plt.ylabel("Distance (m)")
plt.title("Lesson 16: Sensor Noise and Averaging")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("lesson_16_sensor_noise.png", dpi=160)
plt.show()
