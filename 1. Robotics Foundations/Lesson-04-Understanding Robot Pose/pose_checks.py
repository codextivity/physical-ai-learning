"""Physical AI Lesson 04: independent arithmetic checks, not an Isaac Sim test."""
import math


def approx_tuple(a, b, tol=1e-9):
    return all(math.isclose(x, y, abs_tol=tol) for x, y in zip(a, b))


def robot_coordinates(point_world, robot_world_xy, robot_yaw_deg):
    dx = point_world[0] - robot_world_xy[0]
    dy = point_world[1] - robot_world_xy[1]
    angle = math.radians(robot_yaw_deg)
    # Inverse 2D rotation: R(theta)^T * displacement
    return (math.cos(angle)*dx + math.sin(angle)*dy,
            -math.sin(angle)*dx + math.cos(angle)*dy)


def run_checks():
    assert (2 + 2, 3 + 1, 0 + 90) == (4, 4, 90)
    assert approx_tuple(robot_coordinates((7, 5), (3, 2), 0), (4, 3))
    assert approx_tuple(robot_coordinates((7, 5), (3, 2), 90), (3, -4))
    first_pos, second_pos = (2, 1, 1.5), (4, 1, 1.5)
    first_rot, second_rot = (0, 0, 45), (0, 0, 90)
    assert tuple(b-a for a,b in zip(first_pos, second_pos)) == (2, 0, 0)
    assert tuple(b-a for a,b in zip(first_rot, second_rot)) == (0, 0, 45)
    print('PASS: planar pose, aligned/rotated frames, and Isaac Sim target deltas')
    print('NOTE: no USD file was inspected; this is arithmetic validation only.')


if __name__ == '__main__':
    run_checks()
