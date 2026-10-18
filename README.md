# Multiprocess Matrix Multiplier

A small educational Python project that multiplies two randomly generated matrices using multiprocessing. The program asks for matrix dimensions, creates compatible matrices with float entries from -5.0 to 5.0, prints both input matrices, computes the product in parallel, and prints the result.

## Requirements

- Python 3.10 or newer
- No third-party runtime dependencies

## Install

From the repository root, create and activate a virtual environment, then install the package:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

## Run

```bash
matrix-multiplier
```

The original script filename is retained as a convenient alternative:

```bash
python multiprocess_matrix_multiplier.py
```

For multiprocessing programs, keep the application entry point protected by `if __name__ == "__main__":`, especially on Windows and when using the spawn start method.

## How it works

1. The command-line interface prompts for the row and column counts of both matrices. Each dimension must be a positive integer.
2. It checks that the first matrix's column count matches the second matrix's row count.
3. Matrix values are generated randomly as floats between -5.0 and 5.0.
4. Each row of the first matrix is submitted as a separate process-pool task. A task calculates each output cell using the standard row-by-column dot product.
5. Results are returned in input-row order and printed as the result matrix.

The implementation uses a managed `ProcessPoolExecutor`.

## Use the multiplication function

```python
from matrix_multiplier import multiply_matrices_parallel

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
print(multiply_matrices_parallel(matrix_a, matrix_b))
# [[19, 22], [43, 50]]
```

The function raises `ValueError` for empty, non-rectangular, or dimensionally incompatible matrices.

## Tests

```bash
pytest
```

## Project layout

```text
.
├── src/matrix_multiplier/
│   ├── __init__.py
│   ├── cli.py
│   └── core.py
├── tests/test_core.py
├── multiprocess_matrix_multiplier.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```
