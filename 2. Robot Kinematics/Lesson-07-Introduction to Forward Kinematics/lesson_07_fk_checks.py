"""Physical AI Lesson 7: standalone planar forward-kinematics checks.

Uses Python standard library only. This is math verification, NOT Isaac Sim robot control.
"""
import math


def one_link(length_m: float, angle_deg: float) -> tuple[float, float]:
    theta = math.radians(angle_deg)
    return (length_m * math.cos(theta), length_m * math.sin(theta))


def two_link(l1: float, l2: float, theta1_deg: float, theta2_deg: float):
    """theta2_deg is relative to Link1; returns elbow, Link2 center, gripper."""
    t1 = math.radians(theta1_deg)
    t12 = math.radians(theta1_deg + theta2_deg)
    elbow = (l1 * math.cos(t1), l1 * math.sin(t1))
    center = (elbow[0] + l2 / 2 * math.cos(t12),
              elbow[1] + l2 / 2 * math.sin(t12))
    gripper = (elbow[0] + l2 * math.cos(t12),
               elbow[1] + l2 * math.sin(t12))
    return elbow, center, gripper


def assert_xy_close(actual, expected, atol=1e-8):
    assert all(math.isclose(a, b, rel_tol=0, abs_tol=atol)
               for a, b in zip(actual, expected)), (actual, expected)


def main():
    assert_xy_close(one_link(3, 90), (0, 3))
    assert_xy_close(one_link(4, 60), (2, 2 * math.sqrt(3)))
    elbow, center, tip = two_link(3, 2, 0, 60)
    assert_xy_close(elbow, (3, 0))
    assert_xy_close(center, (3.5, math.sqrt(3) / 2))
    assert_xy_close(tip, (4, math.sqrt(3)))
    assert_xy_close(two_link(2, 1, 0, 90)[2], (2, 1))
    assert_xy_close(two_link(2, 1, 40, -20)[0], one_link(2, 40))
    # Validate centered link endpoint reconstruction from the calculated center.
    vx = math.cos(math.radians(60))
    vy = math.sin(math.radians(60))
    assert_xy_close((center[0] - vx, center[1] - vy), elbow)
    assert_xy_close((center[0] + vx, center[1] + vy), tip)
    print(f"Elbow: ({elbow[0]:.3f}, {elbow[1]:.3f}) m")
    print(f"Link2 center: ({center[0]:.3f}, {center[1]:.3f}) m")
    print(f"Gripper X: {tip[0]:.3f} m")
    print(f"Gripper Y: {tip[1]:.3f} m")
    print("All 7 mathematical checks passed.")


if __name__ == "__main__":
    main()
