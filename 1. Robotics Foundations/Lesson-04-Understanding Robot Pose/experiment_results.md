# Lesson 04 - Experiment and Evidence Record

**Lesson:** Understanding Robot Pose  
**Status:** Learner confirmed final USD save; no raw USD or screenshot was supplied.  
**Artifact on learner's PC:** `lesson_04_robot_pose.usd` (not included in this archive).

## Demonstrated in conversation

| Activity | Learner answer / observation | Assessment | Verification basis |
| --- | --- | --- | --- |
| Concept 1: pose changes if orientation changes | Yes; pose changes whenever orientation changes | Correct | Text answer independently checked |
| Concept 2: 2D pose update | (4, 4, 90 degrees) | Correct | Arithmetic independently checked |
| Concept 3: aligned frames | Cup relative to robot (4, 3) | Correct | Arithmetic independently checked |
| Concept 3: rotated robot frame, first attempt | Thought relative coordinates would stay the same | Incorrect initially | Misunderstanding identified and explained |
| Concept 3: retry | Cup robot coordinates change (4, 3) -> (3, -4) | Correct | Frame convention and geometry checked |
| Concept 4: Isaac Sim checkpoint 1 | Set Translate (2, 1, 1.5); Rotate (0, 0, 45), observed movement and rotation | Learner-reported success | Simulator file not supplied |
| Concept 4: Isaac Sim checkpoint 2 | Set Translate X 2 -> 4; Rotate Z 45 -> 90; observed movement and rotation | Learner-reported success | Simulator file not supplied |
| Delta calculation | Delta X +2; delta Z rotation +45 degrees | Correct | Independently checked in code |
| Save scene | Learner said "Done" after save instructions | Learner-confirmed | File not uploaded or independently verified |

## Final expected transform
Translate: (4.0, 1.0, 1.5)  
Rotate: (0, 0, 90 degrees), under the exercise's Euler convention and world-aligned parent assumption.

## Limitations
The USD file is stored on the learner's local computer, not in this package. No independently captured simulator outputs or transform logs are available. The final scene does not by itself demonstrate the intermediate 45-degree rotation; this record documents that intermediate step from conversation reports. The Python checks validate arithmetic and a basic rotated-frame calculation, **not Isaac Sim scene state**.

## Suggested reproducibility check
1. Open the learner's `lesson_04_robot_pose.usd` in Isaac Sim 6.1.
2. Select the cube in Stage and inspect Property > Transform.
3. Confirm displayed final Translate (4, 1, 1.5), Rotate (0, 0, 90 degrees).
4. Inspect whether the cube is directly beneath an untransformed parent before interpreting these as world coordinates.
5. Run `python pose_checks.py` for independent math checks.

**Lesson 5:** Not started.
