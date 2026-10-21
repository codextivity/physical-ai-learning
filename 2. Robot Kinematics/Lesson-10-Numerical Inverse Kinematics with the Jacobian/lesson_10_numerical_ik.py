
import numpy as np
import matplotlib.pyplot as plt

L1, L2 = 3.0, 2.0

target = np.array([2.0, 3.0])
theta = np.deg2rad([10.0, 40.0])

learning_rate = 0.2
tolerance = 1e-4
max_steps = 500

def fk(q):
    t1, t2 = q
    return np.array([
        L1*np.cos(t1) + L2*np.cos(t1+t2),
        L1*np.sin(t1) + L2*np.sin(t1+t2)
    ])

def jacobian(q):
    t1, t2 = q
    return np.array([
        [-L1*np.sin(t1)-L2*np.sin(t1+t2),
         -L2*np.sin(t1+t2)],
        [L1*np.cos(t1)+L2*np.cos(t1+t2),
         L2*np.cos(t1+t2)]
    ])

trajectory = [fk(theta)]

for step in range(max_steps):
    error = target - fk(theta)

    if np.linalg.norm(error) < tolerance:
        break

    delta_theta = learning_rate * (
        np.linalg.pinv(jacobian(theta)) @ error
    )
    theta += delta_theta

    trajectory.append(fk(theta))

trajectory = np.array(trajectory)
final_error = np.linalg.norm(target - fk(theta))

print("Iterations:", step)
print("Shoulder angle:", np.rad2deg(theta[0]))
print("Elbow angle:", np.rad2deg(theta[1]))
print("Final position:", fk(theta))
print("Final error:", final_error)
print("Verification:", "PASSED" if final_error < tolerance else "FAILED")

plt.figure(figsize=(7, 6))
plt.plot(trajectory[:, 0], trajectory[:, 1], "o-", markersize=2,
         label="End-effector path")
plt.scatter(*target, marker="x", s=100, label="Target")
plt.scatter(*trajectory[0], marker="s", s=60, label="Start")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Lesson 10: Numerical Inverse Kinematics")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.savefig("lesson_10_ik_trajectory.png", dpi=160)
plt.show()
