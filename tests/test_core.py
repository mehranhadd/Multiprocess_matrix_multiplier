import pytest

from matrix_multiplier.core import multiply_matrices_parallel


def test_multiply_square_matrices():
    assert multiply_matrices_parallel([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [
        [19, 22],
        [43, 50],
    ]


def test_multiply_rectangular_matrices():
    assert multiply_matrices_parallel([[1, 2, 3], [4, 5, 6]], [[7], [8], [9]]) == [
        [50],
        [122],
    ]


def test_preserves_row_order():
    result = multiply_matrices_parallel([[1, 0], [0, 2], [3, 0]], [[2, 1], [4, 5]])
    assert result == [[2, 1], [8, 10], [6, 3]]


@pytest.mark.parametrize(
    ("matrix_a", "matrix_b"),
    [
        ([], [[1]]),
        ([[1]], []),
        ([[]], [[1]]),
        ([[1, 2], [3]], [[1], [2]]),
        ([[1, 2]], [[1], [2, 3]]),
    ],
)
def test_invalid_matrices_raise_value_error(matrix_a, matrix_b):
    with pytest.raises(ValueError):
        multiply_matrices_parallel(matrix_a, matrix_b)
