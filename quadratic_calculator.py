"""Solve quadratic equations from the command line."""

from __future__ import annotations

import cmath
from typing import tuple


def solve_quadratic(a: float, b: float, c: float) -> tuple[complex, complex]:
    """Return the two roots of ax² + bx + c = 0."""
    if a == 0:
        raise ValueError("a must not be zero for a quadratic equation")

    discriminant = b**2 - 4 * a * c
    square_root = cmath.sqrt(discriminant)
    return (
        (-b + square_root) / (2 * a),
        (-b - square_root) / (2 * a),
    )


def format_root(root: complex) -> str:
    """Format a root without unnecessary complex notation."""
    if abs(root.imag) < 1e-12:
        return f"{root.real:g}"
    return f"{root.real:g} {'+' if root.imag >= 0 else '-'} {abs(root.imag):g}i"


def read_coefficient(name: str) -> float:
    while True:
        try:
            return float(input(f"{name} = "))
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Quadratic equation solver: ax² + bx + c = 0")
    a = read_coefficient("a")
    b = read_coefficient("b")
    c = read_coefficient("c")

    try:
        first_root, second_root = solve_quadratic(a, b, c)
    except ValueError as error:
        print(f"Error: {error}")
        return

    discriminant = b**2 - 4 * a * c
    print(f"Discriminant: {discriminant:g}")
    print(f"x₁ = {format_root(first_root)}")
    print(f"x₂ = {format_root(second_root)}")


if __name__ == "__main__":
    main()
