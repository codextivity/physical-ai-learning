# Physical AI Learning Manual
## Lesson 01: What Is Physical AI?

**Learner background:** AI engineer with Python, deep learning, pose estimation, and action recognition experience; beginner in robotics.

**Status:** Conceptual lesson and guided Python exercise completed. Implementation reviewed logically; local run log not yet submitted.

### Learning objectives
After this lesson, the learner should be able to:
- Explain how Physical AI connects decisions to physical actions and consequences.
- Identify observations, actions, a policy, and the environment.
- Describe a closed perception-action feedback loop.
- Implement a one-dimensional rule-based reaching policy.
- Identify and repair a simple overshoot bug.

### Concept 1: Physical AI and feedback
A perception-only model might label a video as *walking*. A physical AI system can use observations to choose actions that affect a robot and its environment. The distinctive feature is not merely repeated movement: it is updating decisions using observations of what happened.

**Loop:** Observe -> Policy / Decide -> Act -> Environment changes -> Observe again.

### Concept 2: Observations and actions
- **Observation:** sensor information such as camera detections, joint encoder values, or force measurements.
- **Action:** a command, such as moving a joint or closing a gripper.
- **Critical distinction:** commanding an action does not guarantee that its intended physical effect occurred.

**Assessment:** camera detection = observation; gripper-close command = action; force-sensor reading = observation. All three were answered correctly.

### Concept 3: A robot policy
A policy maps available information to a selected action. It can be a simple `if` statement or a learned neural network. The policy in this lesson chooses movement from the measured distance to a cup. A controller and real motors would be additional elements in a physical robot.

### Concept 4: Environment changes and updates
If the gripper is at 6 cm and the cup moves from 10 cm to 15 cm, the new distance is 9 cm. With a maximum step of 2 cm, the next movement is 2 cm. The robot must re-observe the cup instead of relying on the previous target position.

### Guided Python exercise
**Scenario:** a virtual gripper starts at 0 cm and reaches a stationary cup to its right; each action must be no greater than 2 cm.

**Initial learner implementation:** `gripper_position += 2` whenever `distance != 0`. This worked for a target of 10 cm but would overshoot 9 cm and never stop at equality.

**Learner's corrected core logic:**
```python
if distance > 0:
    movement = min(2, distance)
    gripper_position += movement
else:
    print("Gripper reached the cup")
    break
```

**Why `min(2, distance)` matters:** it chooses the smaller of the maximum permitted movement and remaining distance. For 1 cm remaining, it moves 1 cm rather than 2 cm.

The accompanying `robot_policy.py` is a tidy, runnable adaptation. It includes a function wrapper and retains the learner's core policy logic.

### Expected test cases
| Target (cm) | Expected movement positions (cm) |
|---|---|
| 5 | 0 -> 2 -> 4 -> 5 |
| 9 | 0 -> 2 -> 4 -> 6 -> 8 -> 9 |
| 10 | 0 -> 2 -> 4 -> 6 -> 8 -> 10 |
| 15 | 0 -> 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> 15 |

These are **reasoned expectations**, not recorded outputs from learner-run test commands.

### Current limitations
This toy model uses a fixed target, perfect observation, perfect actuation, only one dimension, and an object to the right of the gripper. It does not implement collision checking, grasping, kinematics, actuator limits, or real sensor feedback. Later lessons will address these.

### Learning evidence and mastery status
- Concept 1: explained closed-loop action; refinement needed initially (feedback is not just repetition).
- Concept 2: correctly classified three observations/actions.
- Concept 3: chose action toward the cup and explained why.
- Concept 4: correctly computed 6 cm remaining and identified the need to observe again; subsequently computed 9 cm when the target moved to 15 cm.
- Python exercise: submitted a working-for-10-cm version, recognized the correction after guided explanation, then wrote the bounded step policy.

**Assessment:** introductory conceptual and guided coding objectives achieved. Independent simulation deployment and generalization beyond stated assumptions remain unverified.

### Active-recall questions (try before looking back)
1. What is the difference between repeating an action and using feedback?
2. Label as observation or action: camera coordinates, motor command, gripper force reading.
3. What does a policy do?
4. Why does moving by 2 cm every step fail for a target of 9 cm?
5. With a gripper at 6 cm, a target at 15 cm, and a maximum step of 2 cm, what is the next action and position?

### Review plan
Revisit the five questions about 1 day, 1 week, and 3 weeks after completion; revisit sooner if a question is missed. Run the script locally and attach the output to the experiment record.

### Next topic
**Lesson 02: How Robots Represent Their Environment** - start with 2D coordinate axes, then move gradually toward 3D frames and an Isaac Sim exercise.
