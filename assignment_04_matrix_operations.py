# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols, name="matrix"):
    """Read an rows x cols matrix from the user, one row per line."""
    matrix = []
    for r in range(rows):
        while True:
            raw = input(f"Enter row {r + 1} of {name}: ").split()
            if len(raw) != cols:
                print(f"Error: expected {cols} values, got {len(raw)}. Try again.")
                continue
            try:
                row = [float(x) for x in raw]
                # Store as int if there's no fractional part, for cleaner display
                row = [int(v) if v == int(v) else v for v in row]
                matrix.append(row)
                break
            except ValueError:
                print("Error: please enter numbers only.")
    return matrix


def get_dimensions(prompt_rows="Enter number of rows: ",
                    prompt_cols="Enter number of columns: "):
    """Read positive integer dimensions from the user."""
    while True:
        try:
            rows = int(input(prompt_rows))
            cols = int(input(prompt_cols))
            if rows <= 0 or cols <= 0:
                print("Error: dimensions must be positive integers.")
                continue
            return rows, cols
        except ValueError:
            print("Error: please enter valid integers.")


def transpose_matrix(matrix):
    """Return the transpose of the given matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B using nested loops."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    # Determine the widest element (as a string) for column alignment
    width = max(len(str(value)) for row in matrix for value in row)

    print(f"\n{title}:")
    for row in matrix:
        print("  ".join(str(value).rjust(width) for value in row))


def part_a_transpose():
    print("\n--- PART A: Transpose a Matrix ---")
    rows, cols = get_dimensions()
    matrix = read_matrix(rows, cols)

    result = transpose_matrix(matrix)

    print_matrix(matrix, "Original Matrix")
    print_matrix(result, "Transposed Matrix")


def part_b_add():
    print("\n--- PART B: Add Two Matrices ---")
    rows, cols = get_dimensions()

    print("\nMatrix A:")
    matrix_a = read_matrix(rows, cols, name="Matrix A")

    print("\nMatrix B:")
    matrix_b = read_matrix(rows, cols, name="Matrix B")

    result = add_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(result, "Sum (A + B)")


def part_c_multiply():
    print("\n--- PART C: Multiply Two Matrices ---")

    print("Matrix A dimensions:")
    rows_a, cols_a = get_dimensions()
    matrix_a = read_matrix(rows_a, cols_a, name="Matrix A")

    print("\nMatrix B dimensions (rows of B must equal columns of A):")
    while True:
        rows_b, cols_b = get_dimensions()
        if rows_b != cols_a:
            print(f"Error: Matrix B must have {cols_a} rows to match "
                  f"Matrix A's {cols_a} columns. Try again.")
            continue
        break
    matrix_b = read_matrix(rows_b, cols_b, name="Matrix B")

    result = multiply_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(result, "Product (A x B)")


def main():
    print("=== Matrix Operations ===")
    print("A) Transpose a Matrix")
    print("B) Add Two Matrices")
    print("C) Multiply Two Matrices")

    while True:
        choice = input("\nChoose an operation (A/B/C): ").strip().upper()
        if choice == "A":
            part_a_transpose()
            break
        elif choice == "B":
            part_b_add()
            break
        elif choice == "C":
            part_c_multiply()
            break
        else:
            print("Error: please enter A, B, or C.")


if __name__ == "__main__":
    main()
