"""Interactive command-line interface for the matrix multiplier."""

from __future__ import annotations

import random

from .core import Matrix, multiply_matrices_parallel


def get_numbers(matrix_number: int, dimension: str) -> int:
    """Prompt for matrix dimensions."""
    if matrix_number not in (1, 2):
        raise ValueError("matrix_number must be 1 or 2.")

    while True:
        user_input = input(
            f"Please insert the number of {dimension} of "
            f"{'first' if matrix_number == 1 else 'second'} matrix: "
        )
        if user_input.isdecimal() and 0 < int(user_input):
            return int(user_input)
        print("The input must be a positive integer!")


def matrices_creator() -> tuple[Matrix, Matrix]:
    """Prompt for compatible dimensions and create random matrices.

    Matrix entries are uniformly selected floats from -5.0 through 5.0.
    """
    while True:
        rows_a = get_numbers(1, "Rows")
        columns_a = get_numbers(1, "Columns")
        rows_b = get_numbers(2, "Rows")
        columns_b = get_numbers(2, "Columns")
        if columns_a != rows_b:
            print(
                "To do multiplication, the number of first matrix's columns "
                "must be equal to the second one's rows!"
            )
            continue
        break

    matrix_a = [
        [random.uniform(-5.0, 5.0) for _ in range(columns_a)] for _ in range(rows_a)
    ]
    matrix_b = [
        [random.uniform(-5.0, 5.0) for _ in range(columns_b)] for _ in range(rows_b)
    ]
    return matrix_a, matrix_b


def _print_matrix(title: str, matrix: Matrix) -> None:
    print(title)
    for row in matrix:
        print(row)


def main() -> None:
    """Run the original interactive matrix multiplication workflow."""
    matrix_a, matrix_b = matrices_creator()

    print()
    _print_matrix("Matrix 1:", matrix_a)
    print()
    _print_matrix("Matrix 2:", matrix_b)
    print()

    result = multiply_matrices_parallel(matrix_a, matrix_b)

    print()
    _print_matrix("Result:", result)


if __name__ == "__main__":
    main()
