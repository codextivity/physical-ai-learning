"""Lesson 01: simple 1D observation-policy-action demonstration.

Assumptions: stationary target to the right, perfect sensing and movement.
"""

def reach_cup(cup_position=15, max_step=2):
    gripper_position = 0
    while True:
        distance = cup_position - gripper_position  # Observe
        if distance <= 0:  # Decide whether to stop
            print('Gripper reached the cup')
            break
        movement = min(max_step, distance)  # Policy: choose bounded action
        gripper_position += movement  # Act
        print('Gripper:', gripper_position, 'Cup:', cup_position)
    return gripper_position


if __name__ == '__main__':
    reach_cup(15)
