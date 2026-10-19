
import sys
import shutil
import subprocess
from pathlib import Path

folder = Path(__file__).resolve().parent
controller = folder / "project_01_ik_controller.py"
generated = folder / "project_01_ik_generated.usda"
poses_folder = folder / "generated_poses"
poses_folder.mkdir(exist_ok=True)

print("\n=== Two-Link Robot IK Visualizer ===")
print("Robot: L1 = 3 m, L2 = 2 m")
print("Enter q to quit.")

while True:
    try:
        entry = input("\nTarget X (or q): ").strip()
        if entry.lower() == "q":
            break

        x = float(entry)
        y = float(input("Target Y: "))
        branch = input(
            "Elbow (positive/negative): "
        ).strip().lower()

        if branch not in ("positive", "negative"):
            print("Invalid elbow configuration.")
            continue

        # Call the already-tested IK controller.
        result = subprocess.run(
            [
                sys.executable,
                str(controller),
                str(x),
                str(y),
                branch,
            ],
            check=False,
        )

        if result.returncode != 0:
            print("No pose saved. Try another target.")
            continue

        # Preserve every successful pose.
        index = 1
        while True:
            filename = f"pose_{index:03d}_{branch}.usda"
            destination = poses_folder / filename
            if not destination.exists():
                break
            index += 1

        shutil.copy2(generated, destination)

        print(f"\nSaved pose: {destination}")
        print("Open this file in Isaac Sim to view it.")

    except ValueError:
        print("Please enter numeric coordinates.")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        break
    except OSError as exc:
        print(f"File error: {exc}")
