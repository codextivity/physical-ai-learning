# Physical AI Learning Manual - Lesson 04
## Understanding Robot Pose

**Status:** Completed through user-reported Isaac Sim exercise and checked conversation answers.  
**Platform:** Isaac Sim 6.1 on Windows 11.  
**Scope:** Introductory 2D/3D pose, reference frames, and pose editing; not yet rigid-body transformation mathematics.

### Learning objectives
1. Define pose as a combination of position and orientation.
2. Write a planar pose as (x, y, theta) and an illustrative 3D pose as (x, y, z, roll, pitch, yaw).
3. Distinguish world-frame object coordinates from coordinates expressed in a rotating robot frame.
4. Read and change a cube's position and orientation using Isaac Sim's Transform fields.

### Concept 1 - What is a pose?
A pose specifies **where something is** and **how it is oriented** relative to a chosen reference frame. In a 2D example, a robot initially at (4, 2, 90 degrees) that turns in place to (4, 2, 180 degrees) has a different pose, even though the position is unchanged. The learner answered this correctly.

### Concept 2 - Pose representation
For a robot moving on a plane, use P = (x, y, theta). In our convention, theta = 0 degrees faces world +X and positive angles turn counterclockwise. Example: initial P = (2, 3, 0 degrees), moving +2 in world X, +1 in world Y and rotating +90 degrees gives P = (4, 4, 90 degrees). The learner calculated this correctly. An important refinement: theta_final = theta_initial + signed_angle_change.

For an introductory 3D example, write P = (x, y, z, roll, pitch, yaw). This is a learning shorthand, **not** a convention-independent pose representation. Rotation order, handedness, frame convention and intrinsic/extrinsic interpretation must be specified before exchanging Euler values between systems. Later studies will cover rotation matrices, quaternions, and rigid transforms.

### Concept 3 - Pose and reference frames
**Aligned frames:** Robot world position R = (3, 2); cup world position C = (7, 5). The displacement is C - R = (4, 3). With aligned axes, the cup's robot-frame coordinates are (4, 3).

**Robot rotated 90 degrees counterclockwise around Z:** The robot and cup remain at the same world positions. Relative robot-frame coordinates become (3, -4). Intuitively, the cup is now 3 units forward and 4 units right when robot +X is forward and robot +Y is left. The learner initially thought the relative coordinates would remain unchanged, then corrected their understanding and supplied (4, 3) -> (3, -4) correctly.

The 2D rule for a rotated frame is p_robot = R(theta)^T (p_world - t), where R(theta) rotates vectors from robot coordinates to world coordinates, and t is the robot-frame origin in world coordinates. This formula is included for future reference; **the learner has not yet been assessed on rotation matrices**.

### Concept 4 - Isaac Sim exercise
The learner reported creating a cube in Isaac Sim 6.1 and setting a first pose using the Property > Transform fields:

| Stage | Translate X,Y,Z | Rotate X,Y,Z (degrees) |
| --- | --- | --- |
| Checkpoint 1 | (2, 1, 1.5) | (0, 0, 45) |
| Checkpoint 2 / saved final pose | (4, 1, 1.5) | (0, 0, 90) |

From checkpoint 1 to checkpoint 2: delta X = +2 and delta yaw = +45 degrees; all other shown transform values remain unchanged. The learner calculated both changes accurately, reported the cube moved and rotated, and confirmed saving `lesson_04_robot_pose.usd` locally.

**Frame assumption:** In this simple scene, the cube is assumed to have no transformed parent, so its displayed local Transform values coincide with its world transform. In a scene with transformed ancestors, displayed local values alone cannot establish world pose.

**Evidence limit:** We did not receive the USD file or screenshots, so file existence, scene hierarchy, actual stored transform, and simulator behavior have not been independently inspected. The saved USD generally records the final state, not the sequence of intermediate edits.

### Review questions
1. A robot keeps position (4, 2) but changes yaw from 90 to 180 degrees. Has its pose changed? **Yes: orientation changed.**
2. Start at (2, 3, 0 degrees), move +2 world X and +1 world Y, rotate +90 degrees. Final pose? **(4, 4, 90 degrees).**
3. Robot world position (3, 2), cup world position (7, 5), aligned axes. Cup in robot frame? **(4, 3).**
4. Same positions; robot rotates +90 degrees. Cup in robot frame? **(3, -4).**
5. In Isaac Sim, change X position 2 -> 4 and Z rotation 45 -> 90 degrees. Changes? **+2 position X; +45 degrees Z rotation.**

### Scope and next steps
Demonstrated: conceptual definition of pose, planar pose arithmetic, basic reference-frame intuition, and manual Isaac Sim pose editing as reported. Not demonstrated: composing 3D transforms, quaternion orientation, ROS TF, programming Isaac Sim poses via Python, or validating the saved USD scene programmatically. Lesson 5 is **not started**.
