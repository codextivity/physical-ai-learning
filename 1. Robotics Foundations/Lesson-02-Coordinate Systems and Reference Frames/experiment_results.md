# Lesson 02 — Practical Evidence & Experiment Record

**Date of record:** 2026-10-12  
**Lesson:** How Robots Represent Their Environment  
**Simulator:** Isaac Sim 6.1 (Windows standalone GUI)  
**User-reported saved artifact:** `lesson_02_coordinates.usd` (not uploaded or independently inspected)

## Exercise record

| Checkpoint | Expected | Evidence received | Status |
|---|---|---|---|
| 2D displacement | (2,3)+(2,-1)=(4,2) | Learner gave calculation | Demonstrated in conversation |
| 3D displacement | (2,3,1)+(1,-2,3)=(3,1,4) | Learner gave calculation | Demonstrated in conversation |
| Aligned-frame relative point | (8,5)-(3,2)=(5,3) | Learner selected (5,3) | Demonstrated in conversation |
| Isaac Sim first Translate | (2.0,1.0,1.5) | Learner confirmed cube moved in viewport | User-confirmed |
| Isaac Sim second Translate | (3.0,2.0,2.5) | Learner said verified | User-confirmed |
| Displacement first → second | (1.0,1.0,1.0) | Explained in tutor conversation | Expected calculation; not independently measured |
| Saved USD artifact | lesson_02_coordinates.usd | Learner confirmed save | User-confirmed; file not supplied |

## Reproducibility instructions

1. Open the standalone Isaac Sim 6.1 GUI.
2. Create a stage and add a Cube prim.
3. Set its Transform → Translate to (2.0, 1.0, 1.5), and record a screenshot.
4. Change Translate to (3.0, 2.0, 2.5), and record a screenshot.
5. Save the stage as `lesson_02_coordinates.usd`.
6. Close and reopen the saved stage; inspect the cube's final Translate values.
7. Optionally execute `coordinate_checks.py` to verify the arithmetic outside Isaac Sim.

## Evidence limits

- This documentation was produced from tutorial conversation and learner confirmation. It does not contain the actual `.usd` file.
- The script is a numerical arithmetic check, **not** a program that opens Isaac Sim or reads a USD stage.
- The result does not establish rotated-frame transformations or robot control competency.

## Corrections log

An earlier teaching diagram used the wrong robot-world-origin label `(3, 1)` while the intended example used `(3, 2)`. The consistent example yields cube world `(6, 4)` and robot-relative `(3, 2)` when axes align.
