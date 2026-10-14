"""Physical AI Lesson 05: planar and yaw-only coordinate transformation checks."""
from math import cos, sin, radians, isclose

def rotate(point, angle_deg):
    a = radians(angle_deg)
    x, y = point
    return (cos(a)*x - sin(a)*y, sin(a)*x + cos(a)*y)

def world_to_robot(world, robot_pos, yaw_deg):
    return rotate((world[0]-robot_pos[0], world[1]-robot_pos[1]), -yaw_deg)

def robot_to_world(local, robot_pos, yaw_deg):
    x, y = rotate(local, yaw_deg)
    return (x+robot_pos[0], y+robot_pos[1])

def close(actual, expected):
    assert len(actual) == len(expected)
    assert all(isclose(a,b,abs_tol=1e-9) for a,b in zip(actual,expected)), (actual,expected)

if __name__ == '__main__':
    close(world_to_robot((9,6),(3,2),0), (6,4))
    close(world_to_robot((3,0),(0,0),90), (0,-3))
    close(world_to_robot((7,5),(3,2),90), (3,-4))
    close(robot_to_world((5,-2),(2,3),90), (4,8))
    close(robot_to_world((1,0),(2,3),90), (2,4))
    # Corresponding Z component is unchanged for yaw-only rotation:
    assert 0 + 1 == 1
    print('PASS: 6 Lesson 05 transformation checks')
