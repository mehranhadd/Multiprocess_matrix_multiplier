"""Core matrix operations and process-based multiplication."""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from functools import partial
from collections.abc import Sequence

Matrix = list[list[float]]


def _multiply_row(row: Sequence[float], matrix_b: Sequence[Sequence[float]]) -> list[float]:
    """Multiply one row by matrix B, returning the corresponding result row."""
    result_row: list[float] = []
    for column in range(len(matrix_b[0])):
        total = 0
        for inner_index in range(len(matrix_b)):
            total += row[inner_index] * matrix_b[inner_index][column]
        result_row.append(total)
    return result_row


def _validate_matrix(matrix: Sequence[Sequence[float]], name: str) -> int:
    """Validate a non-empty rectangular matrix and return its column count."""
    if not matrix:
        raise ValueError(f"{name} must contain at least one row.")
    if not matrix[0]:
        raise ValueError(f"{name} must contain at least one column.")

    columns = len(matrix[0])
    for row_number, row in enumerate(matrix, start=1):
        if len(row) != columns:
            raise ValueError(
                f"{name} must be rectangular; row {row_number} has "
                f"{len(row)} columns, expected {columns}."
            )
    return columns


def multiply_matrices_parallel(matrix_a: Sequence[Sequence[float]], matrix_b: Sequence[Sequence[float]]) -> Matrix:
    """Multiply two compatible matrices using one process per row of matrix A.

    Each row is an independent job. ``executor.map`` preserves input order,
    so result rows stay in the same order as rows in ``matrix_a``.
    """
    columns_a = _validate_matrix(matrix_a, "matrix_a")
    _validate_matrix(matrix_b, "matrix_b")

    if columns_a != len(matrix_b):
        raise ValueError(
            "Matrix dimensions are incompatible: the number of columns in "
            "matrix_a must equal the number of rows in matrix_b."
        )

    multiply_with_b = partial(_multiply_row, matrix_b=matrix_b)
    with ProcessPoolExecutor(
        max_workers=len(matrix_a),
        mp_context=multiprocessing.get_context("spawn"),
    ) as executor:
        return list(executor.map(multiply_with_b, matrix_a))
