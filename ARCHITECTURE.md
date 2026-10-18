# Architecture notes

- `src/matrix_multiplier/core.py` contains the multiplication operation and matrix-shape validation. `_multiply_row` is a top-level function so it can be serialized for worker processes.
- `src/matrix_multiplier/cli.py` handles interactive dimension prompts, random matrix creation, printing, and the command-line entry point.
- `multiprocess_matrix_multiplier.py` A thin launcher that re-exports the main public functions.
- `tests/test_core.py` checks expected products, rectangular inputs, row ordering, and invalid shapes without relying on random values.