
import numpy as np

L1, L2 = 3.0, 2.0
theta1 = np.deg2rad(0.0)
theta2 = np.deg2rad(90.0)

joint_velocity = np.array([0.1, 0.2])

J = np.array([
    [
        -L1*np.sin(theta1) - L2*np.sin(theta1+theta2),
        -L2*np.sin(theta1+theta2)
    ],
    [
        L1*np.cos(theta1) + L2*np.cos(theta1+theta2),
        L2*np.cos(theta1+theta2)
    ]
])

gripper_velocity = J @ joint_velocity

print("Jacobian:")
print(np.round(J, 6))
print("\nGripper velocity:", gripper_velocity, "m/s")
print("Jacobian determinant:", np.linalg.det(J))

expected = np.array([-0.6, 0.3])
print("Verification:", "PASSED" if np.allclose(
    gripper_velocity, expected, atol=1e-9
) else "FAILED")
