"""Lesson 02: reproducible coordinate arithmetic (not an Isaac Sim/USD reader)."""


def add(a, b):
    return tuple(x + y for x, y in zip(a, b, strict=True))


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b, strict=True))


def main():
    assert add((2, 3), (2, -1)) == (4, 2)
    assert add((2, 3, 1), (1, -2, 3)) == (3, 1, 4)
    assert subtract((8, 5), (3, 2)) == (5, 3)
    assert subtract((6, 4), (3, 2)) == (3, 2)
    initial = (2.0, 1.0, 1.5)
    final = (3.0, 2.0, 2.5)
    assert subtract(final, initial) == (1.0, 1.0, 1.0)
    print("Lesson 02 coordinate checks: PASSED")
    print("Isaac Sim expected displacement:", subtract(final, initial))


if __name__ == "__main__":
    main()
