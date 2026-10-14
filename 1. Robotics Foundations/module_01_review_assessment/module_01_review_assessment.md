# Physical AI - Module 1 Review Assessment Evidence

**Coverage:** Lessons 1-5 (Robotics Foundations)  
**Assessment:** 10 guided review questions, answered one at a time  
**Source:** Responses and corrections recorded in the project conversation  
**Status:** Module 1 completed; Lesson 6 not started  

## Results summary

- **First-attempt score: 8/10 (80%).**
- **Q7:** Initially incorrect inverse-rotation signs, then corrected after feedback.
- **Q10:** Initially incorrect parent-child calculation, followed by correct separate reinforcement with new numbers.
- **Independent reinforcement:** Parent (4,1,0), yaw +90 degrees; child (3,2,1). Learner computed rotated XY (-2,3) and world point (2,4,1), both correct.
- **Readiness:** Ready to begin Module 2 based on demonstrated performance, while continuing to practice matrix signs and transformation order.

**Evidence qualifier:** This is a faithful compilation of learner-submitted chat answers and assistant-provided evaluations, not a proctored or independently monitored exam. Isaac Sim scenes are not part of this assessment report. Original chat provides the primary record.

## Question-by-question evidence

### Question 1: Closed-loop control

**Question:** A robot gripper detects a cup at 10 cm. During motion, the cup moves to 15 cm. Compare A: continue toward the old target without observing again; B: observe again and adjust. Which is closed-loop control?

**Learner answer:** Strategy B. "Because when the cup position is changed, the whole environment also changes. So, observing the environment again is required."

**Expected result / feedback:** Strategy B: updated observations inform new actions. Refinement: a change to the cup does not mean the entire environment changes.

**First attempt:** Correct first attempt.

### Question 2: Observation, action, policy

**Question:** The camera detects a cup 12 cm away and the controller commands a 2 cm forward motion. Identify the observation, action, and policy.

**Learner answer:** Observation: cup is 12 cm away. Action: move gripper 2 cm. Policy: uses observations to select actions.

**Expected result / feedback:** Observation = distance measurement; action = movement command; policy = rule mapping observations to actions.

**First attempt:** Correct first attempt.

### Question 3: 3D position updates

**Question:** Gripper starts at (2,3,1). It moves 3 units right, 2 backward, and 4 up; +X right, +Y forward, +Z up. Find its final position.

**Learner answer:** (5,1,5). X=2+3; Y=3-2; Z=1+4.

**Expected result / feedback:** (5,1,5).

**First attempt:** Correct first attempt.

### Question 4: Signed rotation and fixed position

**Question:** Gripper position is (4,2,1), orientation +30 deg about Z. It rotates 90 deg clockwise about its own center without translating. Find final orientation and position.

**Learner answer:** Z orientation = -60 deg; position = (4,2,1) unchanged. 30+(-90)=-60.

**Expected result / feedback:** Orientation -60 deg, position unchanged.

**First attempt:** Correct first attempt.

### Question 5: 2D robot pose

**Question:** A mobile robot starts at pose (3,2,45 deg), moves 2 world-X units with world Y unchanged, then rotates 45 deg counterclockwise about its center. Find the final pose.

**Learner answer:** (5,2,90 deg). X=3+2; Y=2+0; "Z"=45+45.

**Expected result / feedback:** (5,2,90 deg). Notation refinement: the third 2D pose component is theta (heading), not Z position.

**First attempt:** Correct first attempt.

### Question 6: Robot and world reference frames

**Question:** Robot world position (2,3); cup world position (8,7). Find cup robot-frame coordinates at yaw 0 deg and after robot yaw +90 deg, with both objects stationary.

**Learner answer:** Before (6,4); after (4,-6). Robot rotation changes local X/Y axes.

**Expected result / feedback:** Before (6,4) by subtraction; after (4,-6) using inverse rotation.

**First attempt:** Correct first attempt.

### Question 7: Inverse rotation matrix

**Question:** Robot at world origin, yaw +90 deg; cube world point (5,2). Compute cube coordinates in the robot frame using R(-90)=[[0,1],[-1,0]].

**Learner answer:** First: (-2,5), with X=0+(-2), Y=5+0. Retry: (2,-5), with X=0+2, Y=-5+0.

**Expected result / feedback:** (2,-5). x=0*5+1*2=2; y=-1*5+0*2=-5. First attempt applied the positive rather than inverse rotation.

**First attempt:** Incorrect first attempt; corrected on retry.

### Question 8: Combined world-to-robot transform

**Question:** Robot world position (2,1), yaw +90 deg; cube world position (6,4). Compute displacement and robot-frame coordinates using inverse rotation.

**Learner answer:** World displacement (4,3); robot-frame (3,-4). X=0+3; Y=-4+0.

**Expected result / feedback:** Displacement (4,3); inverse-rotated point (3,-4).

**First attempt:** Correct first attempt.

### Question 9: Robot-to-world inverse transform

**Question:** Robot world position (3,2), yaw +90 deg; cube robot-frame position (4,-2). Calculate rotated vector and world point.

**Learner answer:** Rotated vector (2,4); world coordinates (5,6).

**Expected result / feedback:** R(+90)*(4,-2)=(2,4); then +(3,2)=(5,6).

**First attempt:** Correct first attempt.

### Question 10: Parent-child transforms

**Question:** Isaac Sim: RobotFrame parent translation (3,2,0), yaw +90 deg; child Cube local position (2,1,1). Find rotated XY and world position.

**Learner answer:** First: rotated XY (-3,5); world (0,7,1). Reasoning: "I am not sure."

**Expected result / feedback:** Rotated XY (-1,2) using (x,y)->(-y,x); world position (2,4,1) after adding translation (3,2,0). Z=1 was correct.

**First attempt:** Incorrect first attempt; later reinforcement passed.

## Targeted reinforcement after Question 10

**Prompt:** Parent translation (4,1,0), yaw +90 degrees; child local position (3,2,1). Find rotated XY and final world position.

**Learner submission:** Rotated XY = (-2,3); world = (2,4,1). Explanation: rotated X = 0 + (-2); Y = 3 + 0; world X = -2 + 4; Y = 3 + 1; Z = 1 + 0.

**Verified calculation:** R(+90)*(3,2)=(-2,3); (-2,3,1)+(4,1,0)=(2,4,1). Correct without needing a further correction on that attempt.

## Recommendations and next steps

1. Continue into Module 2 - Robot Kinematics when ready; do not automatically start Lesson 6.
2. Practice distinguishing active +90-degree vector rotation from world-to-robot inverse rotation.
3. Use the transformation workflow: identify source and target frame, rotate with the proper sign, add or subtract translation in the proper order, and verify results.
4. Keep this assessment with the Module 1 formula handbook and lesson evidence records.

## Key formulas for review

- Signed angle change: delta theta = theta_final - theta_initial.
- World to robot (2D): p_R = R(-theta) (p_W - t).
- Robot to world (2D): p_W = R(+theta) p_R + t.
- R(+90 degrees) maps (x,y) to (-y,x).
- R(-90 degrees) maps (x,y) to (y,-x).

**End of Module 1 review evidence.**
