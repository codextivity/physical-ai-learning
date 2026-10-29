
import numpy as np

# 3D point recovered from the camera
p_camera = np.array([0.4, 0.2, 2.0])

# Camera-to-robot-base rotation: +90 degrees around Z
R_BC = np.array([
    [0.0, -1.0, 0.0],
    [1.0,  0.0, 0.0],
    [0.0,  0.0, 1.0]
])

# Camera origin, expressed in the robot base frame
t_BC = np.array([1.0, 2.0, 0.0])

# Transform camera coordinates into base coordinates
p_base = R_BC @ p_camera + t_BC

# Verify inverse transformation
p_camera_recovered = R_BC.T @ (p_base - t_BC)

# Homogeneous transform equivalent
T_BC = np.eye(4)
T_BC[:3, :3] = R_BC
T_BC[:3, 3] = t_BC

p_homogeneous = np.append(p_camera, 1.0)
p_base_homogeneous = (T_BC @ p_homogeneous)[:3]

print("Camera-frame point:", p_camera)
print("Robot-base point:", p_base)
print("Recovered camera-frame point:", p_camera_recovered)

assert np.allclose(p_base, [0.8, 2.4, 2.0])
assert np.allclose(p_camera_recovered, p_camera)
assert np.allclose(p_base_homogeneous, p_base)

print("Verification: PASSED")
