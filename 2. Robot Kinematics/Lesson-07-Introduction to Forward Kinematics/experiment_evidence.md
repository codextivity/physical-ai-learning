# Lesson 07 - Experiment Evidence Record

## Completion record

- Curriculum: Module 2, Lesson 7 - Forward Kinematics.
- Status: Mathematics, standalone Python, and manually assembled Isaac Sim visualization reported completed; evidence prepared.
- Original user scene file: `lesson_07_forward_kinematics.usda` (saved locally according to learner; **not uploaded to this package**).
- Actual Franka robot was **not** used for Lesson 7's FK validation.

## Direct learner reports

1. One-link FK, L=3 m, angle=90 deg: `(0, 3)` m.
2. One-link FK, L=4 m, angle=60 deg: `(2, 3.464)` m.
3. Relative-angle exercise: shoulder=40 deg, elbow=-20 deg -> Link2 world angle=20 deg.
4. Two-link FK for L1=3, L2=2, shoulder=0 deg, elbow=60 deg: x=4 m and y=1.732 m.
5. Learner's Windows Python terminal output:

       Gripper X: 4.000 m
       Gripper Y: 1.732 m

6. Stage USDA metadata inspected by learner: `metersPerUnit = 1`.
7. `Link1` saved as USD Cube, `size = 1`, translate `(1.5, 0, 0)`, rotate `(0,0,0)`, scale `(3,0.2,0.2)`.
8. `Link2` created alongside Link1 under World, `size = 1`, translate `(3.5,0.866,0)`, rotate `(0,0,60)` degrees, scale `(2,0.2,0.2)`.
9. Learner visually observed both bars meeting at elbow and reported successfully saving the two-link USDA scene.
10. Isaac Sim Script Editor failed for a simple print command, with temp-script-file errors. Cause unresolved; avoided in the FK experiment.

## Independently calculable implications (not simulator measurements)

- Link1 nominal bounds: x=0 to 3 m.
- Expected elbow: `(3, 0, 0)` m.
- Ideal Link2 center: `(3.5, 0.8660254038, 0)` m.
- Expected ideal gripper: `(4, 1.7320508076, 0)` m.
- User's Link2 center Y `0.866` differs from ideal by approximately `-0.0000254` m.
- Reconstructed gripper Y from reported scene transform is about `1.7320254` m; rounded to 3 decimals this is `1.732` m.

## Evidence scope / remaining gaps

- This record is based on learner reports and the lesson conversation. The underlying USDA file was not provided for an independent parse.
- No screenshot of the finished assembly or measured endpoint transform was provided in this turn.
- Two positioned Cube primitives can touch visually but are not a functioning revolute joint or articulated robot.
- Standalone mathematical checks establish equation correctness for test cases, **not** dynamic motion or Isaac Sim physics behavior.

## Suggested archival evidence (optional)

- Add a screenshot showing World/Link1/Link2 and top-down visual alignment.
- Preserve the original `lesson_07_forward_kinematics.usda` next to the package on the user's machine.
- Preserve terminal output of the FK check script.

**Lesson 8:** Not started.
