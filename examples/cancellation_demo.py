"""Compare direct and stable evaluations of sqrt(1+x)-1."""

from minipde.floating_point import (
    direct_sqrt_increment,
    stable_sqrt_increment,
)


def main() -> None:
    """Run the catastrophic cancellation experiment."""
    values = [1.0e-4, 1.0e-8, 1.0e-12, 1.0e-16]

    print(
        f"{'x':>12} "
        f"{'direct':>22} "
        f"{'stable':>22} "
        f"{'relative difference':>22}"
    )

    for x in values:
        direct = direct_sqrt_increment(x)
        stable = stable_sqrt_increment(x)

        relative_difference = abs(direct - stable) / abs(stable)

        print(
            f"{x:12.1e} "
            f"{direct:22.15e} "
            f"{stable:22.15e} "
            f"{relative_difference:22.6e}"
        )


if __name__ == "__main__":
    main()