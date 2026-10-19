
import math
import sys
from pathlib import Path

from pxr import Usd, UsdGeom, Gf

# Robot geometry (meters)
L1 = 3.0
L2 = 2.0

folder = Path(__file__).resolve().parent
source_file = folder / "project_01_two_link_ik.usd"
output_file = folder / "project_01_ik_generated.usda"

# Read target from command line
if len(sys.argv) != 4:
    raise SystemExit(
        "Usage: project_01_ik_controller.py X Y positive|negative"
    )

x = float(sys.argv[1])
y = float(sys.argv[2])
branch = sys.argv[3].lower()

if branch not in ("positive", "negative"):
    raise SystemExit("Choose 'positive' or 'negative'.")

# 1. Reachability
r = math.hypot(x, y)
if not (abs(L1 - L2) <= r <= L1 + L2):
    raise SystemExit(f"Unreachable target: ({x}, {y})")

# 2. Inverse kinematics
c2 = (x*x + y*y - L1*L1 - L2*L2) / (2*L1*L2)
c2 = max(-1.0, min(1.0, c2))

theta2 = math.acos(c2)
if branch == "negative":
    theta2 = -theta2

alpha = math.atan2(y, x)
beta = math.atan2(
    L2 * math.sin(theta2),
    L1 + L2 * math.cos(theta2)
)
theta1 = alpha - beta

# 3. Convert joint angles into cube transforms
elbow_x = L1 * math.cos(theta1)
elbow_y = L1 * math.sin(theta1)

global_angle2 = theta1 + theta2

link1_center = (
    elbow_x / 2,
    elbow_y / 2,
    0
)

link2_center = (
    elbow_x + (L2 / 2) * math.cos(global_angle2),
    elbow_y + (L2 / 2) * math.sin(global_angle2),
    0
)

# 4. Open the existing Isaac Sim scene
stage = Usd.Stage.Open(str(source_file))
if stage is None:
    raise SystemExit(f"Could not open: {source_file}")


def set_transform(path, position, rotation_z):
    prim = stage.GetPrimAtPath(path)

    if not prim.IsValid():
        raise RuntimeError(f"Missing USD prim: {path}")

    xform = UsdGeom.Xformable(prim)

    # Remove existing transform operations.
    # We will rebuild translation, rotation, and scale.
    xform.ClearXformOpOrder()

    
    translate_op = xform.AddTranslateOp(
        precision=UsdGeom.XformOp.PrecisionDouble
    )
    rotate_op = xform.AddRotateXYZOp(
        precision=UsdGeom.XformOp.PrecisionDouble
    )
    scale_op = xform.AddScaleOp(
        precision=UsdGeom.XformOp.PrecisionDouble
    )


    translate_op.Set(Gf.Vec3d(*position))
    rotate_op.Set(Gf.Vec3f(0, 0, rotation_z))

    if path == "/World/Link1":
        scale_op.Set(Gf.Vec3f(3, 0.2, 0.2))
    elif path == "/World/Link2":
        scale_op.Set(Gf.Vec3f(2, 0.2, 0.2))
    else:
        scale_op.Set(Gf.Vec3f(0.15, 0.15, 0.15))


set_transform(
    "/World/Link1",
    link1_center,
    math.degrees(theta1)
)

set_transform(
    "/World/Link2",
    link2_center,
    math.degrees(global_angle2)
)

set_transform(
    "/World/Sphere",
    (x, y, 0),
    0
)

# 5. Export a new scene (preserve the source)
if not stage.GetRootLayer().Export(str(output_file)):
    raise RuntimeError("USD export failed")

# 6. Verify with FK
fk_x = L1 * math.cos(theta1) + L2 * math.cos(global_angle2)
fk_y = L1 * math.sin(theta1) + L2 * math.sin(global_angle2)
error = math.hypot(fk_x - x, fk_y - y)

print(f"Target: ({x:.3f}, {y:.3f})")
print(f"Elbow configuration: {branch}")
print(f"Shoulder angle: {math.degrees(theta1):.3f} deg")
print(f"Elbow angle: {math.degrees(theta2):.3f} deg")
print(f"FK position error: {error:.3e} m")
print(f"Generated scene: {output_file}")
