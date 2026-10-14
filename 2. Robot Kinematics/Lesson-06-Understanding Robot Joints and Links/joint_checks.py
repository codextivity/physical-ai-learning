"""Lesson 06 — Joint configuration and limit checks (pure Python).
These checks verify teaching examples and user-reported UI values; they do
not inspect or simulate the Franka USD asset.
"""
from math import isclose
from dataclasses import dataclass

@dataclass(frozen=True)
class Joint:
    name: str
    kind: str  # 'revolute' or 'prismatic'
    value: float

    def __post_init__(self):
        assert self.kind in {'revolute', 'prismatic'}


def degrees_of_freedom(joints):
    """Count independent one-DOF joints in this simplified model."""
    return len(joints)


def within_limits(angle_deg, lower_deg, upper_deg):
    return lower_deg <= angle_deg <= upper_deg


def run_checks():
    joints = [Joint('shoulder', 'revolute', 0.0),
              Joint('elbow', 'revolute', 0.0),
              Joint('slider', 'prismatic', 0.1)]
    assert degrees_of_freedom(joints) == 3
    assert [j.kind for j in joints] == ['revolute', 'revolute', 'prismatic']
    lower, upper = -101.001, 101.001  # User-reported UI readings
    assert isclose(upper - lower, 202.002, abs_tol=1e-9)
    assert within_limits(0.0, lower, upper)
    assert within_limits(lower, lower, upper)
    assert not within_limits(120.0, lower, upper)
    assert not within_limits(-120.0, lower, upper)
    print('PASS: 6 teaching/example checks; no Isaac Sim asset inspected')

if __name__ == '__main__':
    run_checks()
