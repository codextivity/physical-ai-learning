# Module 3 — Dynamics & Control: Review and Assessment

Lessons 11–15 · Complete after studying Formula Summary. Answers are at the end.

## Learning review
L11: force, torque, inertia, gravitational moment arms.
L12: single-joint equation of motion, gravity compensation, time integration.
L13: P, PD, PID and gravity feedforward.
L14: damping ratio, natural frequency, overshoot and settling.
L15: torque saturation, actuator realism and integral windup.

## Part A — Concept questions (1 point each)
1. A horizontal massless arm holds a point payload. Why is gravitational holding torque greatest at horizontal orientation?
   A) The payload becomes heavier  B) The perpendicular moment arm is largest  C) Inertia disappears
2. For rotation about a fixed axis, net torque produces angular acceleration according to:
   A) tau = I*alpha  B) tau = m*v  C) tau = Kp*e
3. A joint at rest is exactly balanced by the applied motor torque. Its initial angular acceleration is:
   A) Positive  B) Negative  C) Zero
4. In a PD controller with fixed target, the derivative term primarily:
   A) Dampens joint velocity  B) Changes link length  C) Measures torque
5. In the ideal second-order joint model, zeta close to one indicates:
   A) Critical damping  B) No gravity  C) Missing motor
6. Torque is requested as +12 N·m with a ±5 N·m limit. Actual applied torque is:
   A) +12  B) +5  C) -5
7. Integral windup is most directly linked to:
   A) Excessive accumulated control error under saturation  B) Larger rigid-link mass  C) Loss of FK
8. If a PD controller includes accurate angle-dependent gravity compensation, why can a position setpoint remain at rest?
   A) Gravity is disabled  B) The motor counteracts gravity at that angle  C) The mass becomes zero

## Part B — Calculations (2 points each)
9. A 2 kg payload is 0.5 m from a pivot. Compute the magnitude of gravitational torque when horizontal (g=9.81 m/s²).
10. With I=0.5 kg·m², net torque 2 N·m and fixed axis, compute angular acceleration.
11. For I=0.5, b=0.2, Kp=12, Kd=4.7, calculate damping ratio to 3 decimals.
12. For tau_requested=-7 N·m and tau_max=5 N·m, calculate actual torque.

## Part C — Practical verification (4 points)
13. Run `lesson_15_torque_saturation.py`. Report whether saturation occurs and whether both limited and unlimited traces are finite. Save the plot and explain one visible difference. If sharing results, include output or screenshots; do not infer numerical values you did not record.

## Scoring guidance
Part A: 8 points. Part B: 8 points. Part C: 4 points. Total 20 points. Suggested completion standard: 16/20 with no unresolved misunderstanding of torque saturation or net torque. This review is provided for assessment; it is not yet graded.

## Answer key and reasoning
1. B — greatest perpendicular moment arm.
2. A — fixed-axis rotational dynamics tau_net=I*alpha.
3. C — zero net torque means zero instantaneous angular acceleration.
4. A — Kd velocity feedback adds damping.
5. A — critical damping is zeta=1 in the ideal model.
6. B — torque clipped at +5 N·m.
7. A — accumulated integral error continues growing during saturation.
8. B — gravity feedforward cancels the modeled load at the current angle.
9. tau=2*9.81*0.5=9.81 N·m.
10. alpha=tau/I=2/0.5=4 rad/s².
11. zeta=(0.2+4.7)/(2*sqrt(0.5*12))=4.9/(2*sqrt(6))≈1.000.
12. -5 N·m.
13. Expected: saturation count > 0; finite limited trajectory; difference in transient response. Evaluate actual plot and output rather than presuming precise values.

## Learning evidence recorded to date
Lessons 11–15 Python demonstrations were reported as passed. Lesson 11 initially needed reinforcement on moment arm and inertia, which was passed. Lessons 12–15 assessments were passed, including Lesson 15 (Python passed; torque B; windup B). This Module 3 review has not yet been attempted or graded.
