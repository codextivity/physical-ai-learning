# Lesson 03 — Experiment and Evidence Record

**Recorded:** 2026-10-13  
**Application:** NVIDIA Isaac Sim 6.1, Windows GUI  
**Local artifact reported by learner:** `lesson_03_rotation.usd`  
**File uploaded for independent inspection:** No

## 1. Conversational evidence

| Check | Learner response | Evaluation |
|---|---|---|
| Concept 1: rotating a gripper around its own center | Only orientation changes, not position | Correct |
| Concept 2: 45 degrees then 90 degrees clockwise | `45 + (-90) = -45` | Correct |
| Concept 3: turning a cup about vertical Z | Yaw, analogy of turning head left/right | Correct |
| Meaning of signed rotation: 0 to +45 | +45 degrees counterclockwise | Correct |
| GUI: set Rotate Z to 45 | Learner reported cube rotated and Translate remained unchanged | User-confirmed, not independently observed |
| GUI: set Rotate Z to 90 | Learner reported successful setting and answered +45 incremental change | User-confirmed |
| GUI: return Rotate Z to 0 | Learner stated the setting was returned to 0 | User-confirmed |
| Save `lesson_03_rotation.usd` | Learner stated it was saved | User-confirmed |

## 2. Intended values and arithmetic

Translate was to remain (0, 0, 1) throughout. Rotate X = Rotate Y = 0 degrees. Rotate Z followed 0 -> 45 -> 90 -> 0 degrees, with signed increments +45, +45, -90 degrees.

The learner explicitly confirmed unchanged translation at the first rotation, and correctly answered that translation should remain unchanged at 90 degrees. The final exact values were directed but have not been independently inspected.

## 3. Reproducibility

1. Open a fresh Isaac Sim 6.1 scene, create a cube, and inspect Property > Transform.
2. Set Translate to (0, 0, 1), Rotate to (0, 0, 0) degrees.
3. Change only Rotate Z to 45, then 90, then 0 degrees, noting the signed changes.
4. Save as `lesson_03_rotation.usd`.
5. Optionally make screenshots at 45 and 90 degrees for stronger independent evidence.
6. Run `python rotation_checks.py` for arithmetic self-tests (does not connect to Isaac Sim).

## 4. Evidence limits

The USD scene itself, screenshots, simulator logs, and Stage introspection were not provided. Accordingly, no independently verified simulator measurements, file contents, or saved-scene claims are made. The script only checks the mathematics and executes independently of Isaac Sim.

The final USD scene alone will generally show only yaw 0 degrees; the intermediate states are recorded in this Markdown evidence file instead.
