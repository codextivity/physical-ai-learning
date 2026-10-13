# Lesson 01 - Experiment and evidence record

## Provenance
- The learner authored a `while`-loop policy that moved by exactly 2 cm and stopped when distance was zero.
- Tutor feedback highlighted overshoot for targets not divisible by 2.
- Learner revised the policy to `movement = min(2, distance)` and `gripper_position += movement`.
- This package contains a lightly refactored version in `robot_policy.py` (wrapped in a function to make testing easier); it is not a verbatim learner submission.

## Test cases (analytical / expected, not learner-provided execution logs)

| Cup target (cm) | Predicted positions, starting at 0 cm | Expected outcome |
|---|---|---|
| 5 | 0, 2, 4, 5 | Stop at target |
| 9 | 0, 2, 4, 6, 8, 9 | Stop at target |
| 10 | 0, 2, 4, 6, 8, 10 | Stop at target |
| 15 | 0, 2, 4, 6, 8, 10, 12, 14, 15 | Stop at target |

## To reproduce locally
1. Activate your preferred Python environment.
2. Run `python robot_policy.py`.
3. Change `reach_cup(15)` to `reach_cup(9)` and repeat.
4. Save terminal output or a screenshot to the `screenshots/` folder if you wish to add direct execution evidence.

## Status
- Conceptual quizzes: completed in conversation.
- Code review: completed in conversation.
- Automated execution / local output for the revised Python code: **not supplied**.
- Isaac Sim and Isaac Lab installation smoke tests: confirmed in preceding setup conversation; **not demonstrations of this lesson's policy inside a simulator**.
