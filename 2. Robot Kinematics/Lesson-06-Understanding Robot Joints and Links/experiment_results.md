# Lesson 06 — Experiment and Learning Evidence

**Source of evidence:** User responses in this conversation and user-described observations in Isaac Sim 6.1. Joint screenshots were supplied during the conversation, but the final USD scene itself was not uploaded or independently inspected.

## Concept checks
| Concept | Learner response | Evaluation |
|---|---|---|
| Links vs joints | Metal segment is the link; hinge is the joint because it connects links | Correct; joint also constrains relative motion |
| Revolute vs prismatic | Revolute rotates around an axis; prismatic slides | Correct |
| DOF | Three independent one-DOF joints means 3 DOF | Correct under specified assumptions |
| Joint variables | Two rotation angles and one sliding distance | Correct; q=(theta_1,theta_2,d_3) |

## Simulator inspection trace
1. User confirmed finding Isaac Sim robot assets and loading Franka.
2. User found visible links and nested joints. In `panda_link1`, user found `geometry` and `panda_joint2`.
3. User selected `panda_joint2` and identified type as revolute.
4. User provided Body 0 `/World/franka/panda_link1` and Body 1 `/World/franka/panda_link2`.
5. User initially mistook Local Rotation 0/1's multiple XYZ fields for multiple joint axes. After clarification, user found a single Revolute Joint Axis = X.
6. User first reported both limits as +101.001; then corrected and reconfirmed Lower = -101.001 and Upper = +101.001.
7. User confirmed saving `lesson_06_robot_joints.usd` locally.

## Confirmed readings (by user)
| Property | Reading |
|---|---|
| Joint | panda_joint2 |
| Type | Revolute |
| Body 0 | /World/franka/panda_link1 |
| Body 1 | /World/franka/panda_link2 |
| Axis | joint-local X |
| Lower Limit | -101.001 degrees (user-reported) |
| Upper Limit | +101.001 degrees (user-reported) |
| Nominal span | 202.002 degrees (arithmetic only) |

## Verification levels
- **Demonstrated in chat:** accurate conceptual distinctions; user-provided joint/path/axis/limit readings.
- **Code verified here:** joint configuration representation, nominal span arithmetic, and simple one-DOF classification using `joint_checks.py`.
- **Not independently verified:** saved USD contents, unmodified source robot configuration, effective simulated limits, actual articulation movement, joint velocity/torque.
- **Not attempted:** moving the Franka arm or pressing Play. Joint inspection was intentionally read-only.

## Local artifact
The user reported saving `lesson_06_robot_joints.usd` on their Windows PC. This package does **not** contain the USD file. If a future full audit is needed, attach the USD scene and relevant dependencies.

## Progress
Module 1: Lessons 1–5 completed. Module 2: Lesson 6 completed and documented. Lesson 7 not started.
