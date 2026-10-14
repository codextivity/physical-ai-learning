# Lesson 05 — Experiment and Evidence Record

## Evidence status
- Chat calculations: directly demonstrated in conversation and checked against formulas.
- Isaac Sim GUI operations: user-reported; not independently inspected by file or screenshot.
- USD scene saved: user-confirmed as `lesson_05_coordinate_transformations.usd` on their own PC; no USD file was provided for inspection.
- Python transformation tests: reproducible code included; execution status recorded below.

## Learner's demonstrated calculations
| Exercise | Learner result | Assessment |
|---|---|---|
| Translation: world cube (9,6), robot (3,2) | (6,4) | Correct |
| World to rotated robot: world cube (3,0), yaw +90 | (0,-3) | Correct; notation refined |
| Combined world->robot: robot (3,2), yaw +90, cube (7,5) | displacement (4,3), robot (3,-4) | Correct |
| Robot->world: robot (2,3), yaw +90, local (5,-2) | rotated (2,5), world (4,8) | Correct |

## Isaac Sim 6.1 checkpoints (user-confirmed)
1. `RobotFrame` Xform, Translate (2,3,0), Rotate (0,0,0).
2. `Cube` child of RobotFrame, local Translate (1,0,1), Rotate (0,0,0); computed world position (3,3,1).
3. Parent Rotate Z changed from 0 to 90 degrees. Cube moved while its local Translate remained (1,0,1); expected world position (2,4,1).
4. User reported saving `lesson_05_coordinate_transformations.usd`.

## Limitations
The scene contains the final configuration; it is not a time-series record of the earlier state. Exact file content, transforms, rendering, and save destination require later examination of the user's USD file. A cube's shape and camera perspective may affect visible movement, so reported movement is not the same as a measured global transform.

## Reproduction
Run `python transformation_checks.py`. To verify the scene independently, open the USD in Isaac Sim, inspect Stage hierarchy and parent/child transforms, and query the cube's world transform; expected world translation is (2,4,1).
