# Lesson 11 — Introduction to Robot Dynamics

**Physical AI · Module 3: Dynamics & Control · Accelerated lesson manual**  
**Status:** Completed after Python experiment and targeted conceptual reinforcement (2026-10-19)

## Learning outcomes

- Distinguish kinematics (geometry of motion) from dynamics (how forces and torques cause motion).
- Explain mass, force, angular acceleration, torque, and moment of inertia with correct units.
- Calculate gravitational torque for a point-mass payload on a simple arm.
- Explain why a horizontal arm generally requires more gravitational holding torque than a vertical arm.
- Validate the relationship with Python and a torque-versus-angle plot.

## 1. Kinematics versus dynamics

**Kinematics:** joint positions, velocities, accelerations, forward kinematics, inverse kinematics, Jacobians. It does not by itself determine the actuator forces needed to create motion.

**Dynamics:** masses, moments of inertia, forces, torques, contact forces and their relationship to acceleration. Dynamics is required when selecting actuators and designing controllers for gravity and payloads.

## 2. Essential formulas and units

| Idea | Formula | Units / meaning |
|---|---|---|
| Newton's second law | `F_net = m * a` | force N; mass kg; acceleration m/s^2 |
| Fixed-axis rotation | `tau_net = I * alpha` | torque N*m; inertia kg*m^2; angular acceleration rad/s^2 |
| Weight | `W = m * g` | gravitational force N, typically g = 9.81 m/s^2 |
| Point-load gravity torque | `tau_g = m * g * L * cos(theta)` | theta measured from horizontal; signed expression assumes a defined torque direction |
| Horizontal arm | `abs(tau_g) = m * g * L` | maximum gravity moment magnitude in the stated model |
| Vertical arm | `tau_g = 0` | gravity line of action passes through the pivot |

**Assumptions for the gravity-torque example:** planar rotation in a vertical plane; fixed joint axis normal to the plane; rigid, massless arm; point-mass payload at distance `L`; no friction or other external loads; quasistatic holding. The motor's balancing torque acts opposite to gravity. A real arm's own mass, inertia, friction, acceleration and gearing also matter.

## 3. Worked example

For payload `m = 2 kg`, distance `L = 0.5 m`, gravity `g = 9.81 m/s^2`:

`m*g*L = 2 * 9.81 * 0.5 = 9.81 N*m`

| Arm angle from horizontal | Gravity torque magnitude |
|---|---:|
| 0 deg | 9.810 N*m |
| 30 deg | 8.496 N*m |
| 60 deg | 4.905 N*m |
| 90 deg | 0.000 N*m |

**Why torque changes:** payload weight stays the same, but the perpendicular lever arm between the pivot and the gravitational line of action shrinks as the arm approaches vertical.

## 4. Python practical: gravity torque versus angle

Save as `lesson_11_gravity_torque.py` and run with NumPy and Matplotlib installed.

```python
import numpy as np
import matplotlib.pyplot as plt

mass = 2.0       # kg
length = 0.5     # m
gravity = 9.81   # m/s^2

angles_deg = np.linspace(0, 90, 181)
angles_rad = np.deg2rad(angles_deg)
torque = mass * gravity * length * np.cos(angles_rad)

for angle in [0, 30, 60, 90]:
    value = mass * gravity * length * np.cos(np.deg2rad(angle))
    print(f"Angle {angle:2d} deg: {value:.3f} N*m")

assert np.isclose(torque[0], 9.81)
assert np.isclose(torque[-1], 0.0, atol=1e-10)
print("Verification: PASSED")

plt.figure(figsize=(8, 5))
plt.plot(angles_deg, torque)
plt.xlabel("Arm angle from horizontal (degrees)")
plt.ylabel("Gravity torque magnitude (N*m)")
plt.title("Lesson 11: Payload Gravity Torque")
plt.grid(True)
plt.tight_layout()
plt.savefig("lesson_11_gravity_torque.png", dpi=160)
plt.show()
```

**Run:** `python lesson_11_gravity_torque.py`

**Expected checks:** torque 9.810 N*m at 0 deg; ~8.496 N*m at 30 deg; 4.905 N*m at 60 deg; near zero at 90 deg; verification passes; saved figure has a declining cosine-shaped curve.

## 5. Connection to Isaac Sim

The preceding two-link IK project used visual cubes with authored transforms rather than physics-driven joints. Its successful FK/IK pose verification does not demonstrate gravitational torque or motor control. Later Module 3 work will add articulated joints, gravity and actuators to compare required torques with simulated behavior.

## 6. Assessment and recorded outcome

- **Python torque experiment:** user reported `PASSED`.
- **First conceptual attempt:** incorrectly attributed torque differences to changing payload mass, and selected end-effector position rather than inertia.
- **Targeted reinforcement:** both questions answered correctly: (1) gravitational moment arm shrinks as arm rises; (2) moment of inertia relates net fixed-axis torque to angular acceleration.
- **Final lesson status:** **Completed**. Results reflect reported outputs, not independently inspected local screenshots or Python source files.

## 7. Quick review

1. Does the payload weigh less when a robot arm points upward? **No.** Gravity force is still `m*g`.
2. Why does gravitational torque vanish at vertical? **Zero perpendicular moment arm** about the pivot in the simplified model.
3. What does larger `I` imply for the same `alpha`? **Greater net required torque**, via `tau_net = I*alpha`.
4. Is zero gravitational holding torque the same as zero total motor torque during motion? **No.** Acceleration, friction and other effects can still demand torque.

## Next lesson

**Lesson 12 — Robot Equations of Motion:** combine inertia, damping and gravity in a simple one-joint equation and simulate its response numerically.
