
import numpy as np

# Camera intrinsics (pixels)
fx, fy = 600.0, 600.0
cx, cy = 320.0, 240.0

# Known point in the camera frame (meters)
point_3d = np.array([0.4, 0.2, 2.0])
X, Y, Z = point_3d

# 3D -> 2D projection
u = fx * X / Z + cx
v = fy * Y / Z + cy

print(f"Projected pixel: ({u:.1f}, {v:.1f})")

# 2D pixel + known depth -> 3D back-projection
X_recovered = (u - cx) * Z / fx
Y_recovered = (v - cy) * Z / fy

recovered = np.array([X_recovered, Y_recovered, Z])

error = np.linalg.norm(recovered - point_3d)

print("Original 3D point:", point_3d)
print("Recovered 3D point:", recovered)
print(f"Reconstruction error: {error:.3e} m")

assert np.allclose(recovered, point_3d, atol=1e-9)
print("Verification: PASSED")
