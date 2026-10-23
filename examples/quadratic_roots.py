"""Compare two algorithms for the quadratic equation."""

from __future__ import annotations

import math


def roots_standard(
    a: float,
    b: float,
    c: float,
) -> tuple[float, float]:
    """Calculate quadratic roots using the standard expression."""
    discriminant = math.sqrt(b * b - 4.0 * a * c)

    root_1 = (-b + discriminant) / (2.0 * a)
    root_2 = (-b - discriminant) / (2.0 * a)

    return root_1, root_2


def roots_stable(
    a: float,
    b: float,
    c: float,
) -> tuple[float, float]:
    """Calculate quadratic roots avoiding catastrophic cancellation."""
    discriminant = math.sqrt(b * b - 4.0 * a * c)

    q = -0.5 * (
        b + math.copysign(discriminant, b)
    )

    root_1 = q / a
    root_2 = c / q

    return root_1, root_2


def residual(
    root: float,
    a: float,
    b: float,
    c: float,
) -> float:
    """Calculate the absolute polynomial residual."""
    return abs(a * root * root + b * root + c)


def main() -> None:
    """Compare the standard and stable algorithms."""
    a = 1.0
    b = 1.0e8
    c = 1.0

    algorithms = {
        "standard": roots_standard,
        "stable": roots_stable,
    }

    for name, algorithm in algorithms.items():
        roots = algorithm(a, b, c)

        print(f"\nAlgorithm: {name}")

        for index, root in enumerate(roots, start=1):
            value = residual(root, a, b, c)

            print(
                f"root {index}: {root: .17e}"
                f"    residual: {value: .5e}"
            )

        print(f"product: {roots[0] * roots.17e}")


if __name__ == "__main__":
    main()