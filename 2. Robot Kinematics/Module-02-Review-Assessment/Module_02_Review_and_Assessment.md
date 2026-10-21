# Module 2 - Robot Kinematics: Review and Assessment

**Curriculum:** Physical AI | **Lessons:** 6-10 | **Recommended time:** 20-30 minutes

## Review checklist

- [ ] Distinguish links, revolute/prismatic joints, and DOF.
- [ ] Compute XY position with two-link FK.
- [ ] Test target reachability and distinguish the two IK elbow branches.
- [ ] Explain the Jacobian as a mapping from joint velocities to end-effector velocity.
- [ ] Explain why a singular Jacobian restricts Cartesian motion without freezing the joints.
- [ ] Describe the iterative numerical IK loop and its stopping criterion.

## Part A - Knowledge check (1 point each)

**Q1.** A serial planar arm has three independent revolute joints. How many joint DOFs? (A) 1, (B) 3, (C) 6

**Q2.** Which best describes forward kinematics? (A) Joint coordinates -> end-effector pose, (B) Target pose -> joint coordinates, (C) Forces -> torques

**Q3.** For `L1=3 m`, `L2=2 m`, which target radial distance is geometrically unreachable? (A) `0.5 m`, (B) `3 m`, (C) `5 m`

**Q4.** If a two-link planar Jacobian is singular, what follows? (A) All joints are locked, (B) Some instantaneous Cartesian velocity directions are unavailable, (C) Link lengths are zero

**Q5.** Why does numerical IK recalculate position error each iteration? (A) The current gripper position changes, (B) Link lengths change, (C) The Jacobian is always constant

**Q6.** Why can one reachable XY target have two analytical IK solutions? (A) Different elbow configurations, (B) Gravity changes length, (C) FK is random

**Q7.** In `p_dot = J*q_dot`, what are the units of `p_dot` for planar XY position? (A) rad/s, (B) m/s, (C) N*m

**Q8.** For `L1=3`, `L2=2`, `theta1=0`, `theta2=90 deg`, what is `(x,y)`? (A) `(5,0)`, (B) `(3,2)`, (C) `(2,3)`

## Part B - Short calculations (2 points each)

**Q9. FK:** With `L1=3`, `L2=2`, `theta1=0 deg`, `theta2=90 deg`, calculate `x` and `y`, showing substitutions.

**Q10. Reachability:** For `L1=4`, `L2=2`, state the complete geometric radial reach interval. Is a target 1 m from the base reachable?

**Q11. Jacobian velocity:** Given `J=[[-2,-2],[3,0]]`, `q_dot=[0.1,0.2] rad/s`, compute `p_dot`.

**Q12. Singularity:** Explain what `det(J)=0` means for planar 2D instantaneous gripper motion, and why the joints may still move.

## Part C - Practical verification (4 points)

Using your Lesson 10 numerical IK script, change the target to `(3,2)` with `L1=3` and `L2=2`. Record: initial angles; final angles; iterations; final Cartesian error; whether the solver met its tolerance; and one screenshot of the trajectory. Joint angles can differ by elbow branch or equivalent angle wrapping. Briefly explain what changes if initialized near a singular configuration.

## Scoring

- Part A: 8 points.
- Part B: 8 points.
- Part C: 4 points.
- **Total: 20 points.** Suggested strong-pass threshold: 16/20, with correct understanding of FK vs IK, reachability, and singularities.

## Historical Module 2 assessment record

The completed in-chat assessment scored **3/5** initially. Incorrect concepts were FK vs IK and inner-bound reachability. A focused two-question reinforcement was completed with both answers correct, after which Module 2 was marked complete. This worksheet is an additional reusable review resource, **not a claim that its questions have been attempted**.

---

# Instructor / Self-check Answer Key

**Q1:** B (3 independent joint coordinates).

**Q2:** A (FK maps joint coordinates to end-effector pose).

**Q3:** A (reachable `1 <= r <= 5`; `0.5 m` is too close).

**Q4:** B (Jacobian loses rank; not all instantaneous XY motions attainable).

**Q5:** A (the current state and therefore target error change).

**Q6:** A (positive/negative relative elbow angle for many targets).

**Q7:** B (`m/s`).

**Q8:** B (`(3,2)`).

**Q9:** `x=3*cos(0)+2*cos(90 deg)=3`, `y=3*sin(0)+2*sin(90 deg)=2` meters.

**Q10:** `abs(4-2) <= r <= 4+2`, i.e. `2 <= r <= 6` meters; `r=1` is unreachable.

**Q11:** `p_dot=[-2*0.1-2*0.2, 3*0.1+0*0.2]=[-0.6,0.3] m/s`.

**Q12:** Jacobian rank drops, so at least one Cartesian velocity direction is unavailable instantaneously; joints may still rotate and produce motion along remaining directions.

**Part C rubric (4):** 1 point successful target/error evidence; 1 correct program output; 1 trajectory screenshot; 1 accurate explanation of near-singular numerical sensitivity. Avoid promising convergence from every initial state.
