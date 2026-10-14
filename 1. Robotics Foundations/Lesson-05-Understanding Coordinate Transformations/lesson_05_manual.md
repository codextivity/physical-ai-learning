# Physical AI Learning Manual — Lesson 05
## Coordinate Transformations

**Status:** Completed exercises and user-confirmed Isaac Sim experiment; USD file stored locally and not independently inspected.

### Learning goals
- Convert coordinates between aligned frames with translation.
- Understand the distinction between rotating a point and changing a reference frame.
- Use a 2D rotation matrix for world-to-robot and robot-to-world conversions.
- Combine translation and rotation, then apply the idea to parent-child transforms in Isaac Sim 6.1.

### Concept 1 — Translation-only transformations
With world-aligned axes, object coordinates relative to a robot are obtained by subtracting the robot's world position:

    p_robot = p_world - t_robot

Worked problem: robot (3,2), cube (9,6) -> cube robot-frame (9-3, 6-2) = (6,4). The learner computed (6,4) with both subtractions correctly.

### Concept 2 — Rotation of a coordinate frame
For a positive counterclockwise angle theta in the XY plane, the active rotation matrix is:

    Rot(theta) = [[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]

A rotated robot frame requires the inverse (transpose) rotation when expressing a fixed world vector in robot coordinates:

    p_robot = Rot(-theta) * (p_world - t_robot)

At theta = +90 degrees:

    Rot(+90) = [[0,-1],[1,0]]
    Rot(-90) = [[0,1],[-1,0]]

Example: robot at (0,0), yaw +90, cube world (3,0): robot coordinates = (0,-3). The learner obtained (0,-3), with minor notation corrected from '1-(3)' to '(-1)*(3)'.

### Concept 3 — Combined transformations and the inverse
World to robot:

    p_robot = Rot(-theta) * (p_world - t_robot)

Robot to world:

    p_world = Rot(theta) * p_robot + t_robot

Worked example: robot t=(3,2), theta=+90, cup world=(7,5). First subtract -> (4,3). Then inverse-rotate -> (3,-4). The learner independently calculated both.

Inverse worked example: robot t=(2,3), theta=+90, cube robot=(5,-2). Rotate -> (2,5), then translate -> world=(4,8). The learner independently calculated both.

**Important convention:** theta describes robot frame yaw counterclockwise relative to world; all example XY coordinate systems are right-handed with world +Z upward. Order matters: world to robot subtracts translation BEFORE inverse rotation; robot to world rotates BEFORE adding translation.

### Concept 4 — Isaac Sim parent-child transforms
The learner reported creating an Xform named `RobotFrame` as the parent of `Cube` in Isaac Sim 6.1.

Initial configuration:

    RobotFrame world Translate (2,3,0), Rotate (0,0,0 degrees)
    Cube local Translate (1,0,1), Rotate (0,0,0 degrees)
    Expected Cube world position: (3,3,1)

Final configuration:

    RobotFrame world Translate (2,3,0), Rotate (0,0,90 degrees)
    Cube local Translate (1,0,1), Rotate (0,0,0 degrees)
    Expected Cube world position: (2,4,1)

The learner confirmed the cube moved when its parent rotated, while the cube's local Translate stayed (1,0,1). They correctly explained that the parent's local +X axis rotates to world +Y. The local coordinate stays fixed while the world coordinate changes.

**Saved scene:** `lesson_05_coordinate_transformations.usd` — user-confirmed saved locally; the USD itself was not uploaded, so the authored hierarchy and global transforms were not independently verified from USD data.

### Formula summary
- Translation only, aligned axes: `p_robot = p_world - t_robot`.
- Active 2D point rotation: `Rot(theta) = [[cos,-sin],[sin,cos]]`.
- World to robot: `p_robot = Rot(-theta) (p_world - t_robot)`.
- Robot to world: `p_world = Rot(theta) p_robot + t_robot`.
- Parent to world (3D yaw-only): `p_world = Rz(yaw) p_local + t_parent`.

### Self-review questions
1. Why does a fixed object's robot-frame coordinate change when the robot rotates?
2. When converting world to robot, which operation comes first?
3. What does the inverse rotation do?
4. A frame is at (2,3,0) with yaw +90 degrees; what world position corresponds to local (1,0,1)?
5. Does moving a child in world coordinates imply its local Translate changed?

### Lesson completion boundary
Lesson 5 is documented. The completion record is based on independent chat calculations and user-reported simulator actions. Lesson 6 has not started.
