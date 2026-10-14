# Physical AI Learning Manual — Lesson 06
## Robot Links, Joints, and Degrees of Freedom

**Module:** 2 — Robot Kinematics  
**Status:** Lesson concepts passed; hands-on Franka joint inspection user-confirmed; USD saved locally, not uploaded or independently inspected.  
**Simulator:** NVIDIA Isaac Sim 6.1 (Windows)

## Learning goals
1. Distinguish rigid links from the joints connecting them.
2. Recognize revolute (rotating) and prismatic (sliding) joints.
3. Explain degrees of freedom (DOF) and represent a joint configuration.
4. Inspect a real revolute joint's connected bodies, local axis, and limits in Isaac Sim.

## Concept 1 — Links and joints
A **link** is a rigid component of a robot (such as a robot forearm). A **joint** connects bodies and specifies allowable relative motion. A hinge-like joint is a simple example. In Lesson 6 the learner correctly classified a rigid metal segment as a link and its connecting rotating hinge as a joint.

## Concept 2 — Two joint types
- **Revolute joint:** permits rotation about a specified joint axis. Its coordinate is an angle (theta), expressed in degrees or radians.
- **Prismatic joint:** permits translation along a specified joint axis. Its coordinate is a displacement (d), generally expressed in length units.

A door hinge and a sliding drawer are useful analogies. Both idealized joint types provide one DOF each.

## Concept 3 — Degrees of freedom and joint space
A degree of freedom is an independent variable used to describe a mechanism's configuration. For a robot with two independent revolute joints and one independent prismatic joint:

    q = (theta_1, theta_2, d_3)      DOF = 3

The learner correctly answered both 3 DOF and the mixed joint-variable representation. This count assumes each joint contributes one independent motion variable without additional coupling constraints.

Joint-space coordinates q describe joint configuration, whereas Cartesian coordinates p=(x,y,z) describe a point's location. **Forward kinematics** converts q into positions/poses of links or the gripper; this is a future topic, not yet demonstrated.

## Concept 4 — Isaac Sim 6.1: Inspecting a Franka robot
The learner reported loading a Franka asset from the Content Browser and expanding its Stage hierarchy. Observed entries included `panda_link0` through `panda_link7`, `panda_hand`, and finger components. Under `panda_link1` the learner found `geometry` and `panda_joint2`.

The learner inspected `panda_joint2` and reported:

| Field | User-confirmed reading |
|---|---|
| Joint kind | Revolute |
| Body 0 | `/World/franka/panda_link1` |
| Body 1 | `/World/franka/panda_link2` |
| Revolute axis | X (joint-local axis) |
| Lower limit | -101.001 degrees |
| Upper limit | +101.001 degrees |

**Key distinction:** The joint's local attachment orientations (Local Rotation 0 and 1) are not additional degrees of freedom. Axis X designates rotation around the **joint-local** X-axis, which need not align with the world's X-axis.

## Motion limits
For a revolute joint with finite angular limits:

    theta_min <= theta <= theta_max
    angular_range = theta_max - theta_min

With the user-reported values, the nominal configured range is:

    101.001 - (-101.001) = 202.002 degrees

This is an arithmetic interpretation of the UI readings, **not an independent validation** of the source asset's authoritative limits or the physical behavior. The user briefly suspected misreading/editing the sign, then reconfirmed the pair. No joint movement or simulation-based limit test was performed.

## Practical workflow (reproducible)
1. Launch Isaac Sim 6.1 and create a new stage.
2. In Content Browser, find and load an articulated Franka robot.
3. Expand the Stage hierarchy and locate `panda_link1/panda_joint2`.
4. Select `panda_joint2`; inspect joint type, Body 0, Body 1.
5. Locate **Revolute Joint** properties and record its Axis and lower/upper limits.
6. Do not alter limits or press Play for this observational exercise.
7. Save As `lesson_06_robot_joints.usd`.

**Actual output:** The learner confirmed saving `lesson_06_robot_joints.usd` locally. The USD file was not uploaded and is not inside this documentation package.

## Common pitfalls
- The Stage hierarchy is not the same thing as the graph of mechanical joint connections; inspect Body 0/Body 1 relationships.
- Local Rotation 0/1 are attachment-frame orientations, not multiple permitted joint axes.
- Do not assume the joint-local axis points along the corresponding world axis.
- A joint count equals DOF only under the stated independence and constraint assumptions.
- Recorded property values are not proof that the joint physically moved through the full limit range.

## Review questions
1. How is a link different from a joint?
2. Which variable describes a revolute joint? Which describes a prismatic joint?
3. What does q=(theta_1,theta_2,d_3) represent?
4. What do Body 0 and Body 1 tell you about a physics joint?
5. Why does Axis X not guarantee rotation about the world's X-axis?
6. Why is reading a joint limit different from testing its actual dynamic range?

## Next lesson
Lesson 7 is **not started**. No claims of forward-kinematics competence are made on the basis of this lesson alone.
