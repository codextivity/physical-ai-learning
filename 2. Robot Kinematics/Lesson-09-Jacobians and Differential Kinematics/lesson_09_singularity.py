
import numpy as np

L1, L2 = 3.0, 2.0

def jacobian(theta1_deg, theta2_deg):
    t1 = np.deg2rad(theta1_deg)
    t2 = np.deg2rad(theta2_deg)

    return np.array([
        [
            -L1*np.sin(t1) - L2*np.sin(t1+t2),
            -L2*np.sin(t1+t2)
        ],
        [
            L1*np.cos(t1) + L2*np.cos(t1+t2),
            L2*np.cos(t1+t2)
        ]
    ])

# Compare three elbow configurations.
for elbow in [90, 5, 0]:
    J = jacobian(0, elbow)

    determinant = np.linalg.det(J)
    rank = np.linalg.matrix_rank(J)

    print(f"\nElbow angle: {elbow} degrees")
    print("Jacobian:\n", np.round(J, 6))
    print(f"Determinant: {determinant:.6f}")
    print(f"Rank: {rank}")
    print("Singular:", rank < 2)

# Verify the exactly straight-arm Jacobian.
J_straight = jacobian(0, 0)
expected = np.array([[0.0, 0.0],
                     [5.0, 2.0]])

assert np.allclose(J_straight, expected)
assert np.linalg.matrix_rank(J_straight) == 1

print("\nSingularity verification: PASSED")
