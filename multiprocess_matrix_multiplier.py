"""Compatibility entry point; run the installed package's interactive CLI."""

from matrix_multiplier.cli import get_numbers, main, matrices_creator
from matrix_multiplier.core import multiply_matrices_parallel

__all__ = ["get_numbers", "main", "matrices_creator", "multiply_matrices_parallel"]


if __name__ == "__main__":
    main()
