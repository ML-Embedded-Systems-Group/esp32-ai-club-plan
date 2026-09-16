"""Compare student_forward.forward to the frozen golden logits."""

from pathlib import Path

import numpy as np

from student_forward import forward

HERE = Path(__file__).resolve().parent
LAB = HERE
if not (HERE / "weights.npz").exists():
    LAB = Path(__file__).resolve().parents[3] / "tasks" / "week-3" / "lab"
    if not (LAB / "weights.npz").exists():
        LAB = Path(__file__).resolve().parent


def main():
    weights = dict(np.load(LAB / "weights.npz"))
    idx = np.load(LAB / "idx.npy")
    golden = np.load(LAB / "golden_logits.npy")
    out = forward(weights, idx)
    out = np.asarray(out, dtype=np.float32)
    if out.shape != golden.shape:
        print(f"FAIL shape student={out.shape} golden={golden.shape}")
        return 1
    diff = np.max(np.abs(out - golden))
    print(f"max abs diff = {diff:.8e}")
    if diff < 1e-5:
        print("PASS")
        return 0
    print("FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
