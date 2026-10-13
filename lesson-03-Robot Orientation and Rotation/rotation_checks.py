"""Lesson 03: independent checks of planar signed-rotation arithmetic.

This script does not read Isaac Sim or USD files.
"""

def signed_change(initial_deg: float, final_deg: float) -> float:
    """Raw difference for a known, unwrapped rotation sequence."""
    return final_deg - initial_deg


def run_checks() -> None:
    sequence = [0, 45, 90, 0]
    changes = [signed_change(a, b) for a, b in zip(sequence, sequence[1:])]
    assert changes == [45, 45, -90], changes
    assert 45 + (-90) == -45
    assert 0 + 45 == 45
    assert -30 + 90 == 60
    assert sum(changes) == 0
    print("PASS: yaw states (degrees):", sequence)
    print("PASS: signed changes (degrees):", changes)
    print("PASS: initial and final yaw are both 0 degrees")
    print("NOTE: This checks arithmetic only, not the user's saved Isaac Sim USD.")


if __name__ == "__main__":
    run_checks()
