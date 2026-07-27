def print_single_table(number):
    """PART A: Print the multiplication table for `number` from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number}  x  {i:<2} =  {result}")


def print_tables_up_to_n(n):
    """PART B: Print multiplication tables for every number from 1 to N."""
    for number in range(1, n + 1):
        print_single_table(number)
        if number != n:
            print("-" * 27)


def get_positive_integer(prompt):
    """Read a positive integer from the user; return None if invalid."""
    try:
        value = int(input(prompt))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return None

    if value <= 0:
        print("Error: N must be a positive integer.")
        return None

    return value


def main():
    print("--- PART A: Single Table ---")
    number = get_positive_integer("Enter a number: ")
    if number is None:
        return
    print_single_table(number)

    print("\n--- PART B: Tables from 1 to N ---")
    n = get_positive_integer("Enter N: ")
    if n is None:
        return
    print_tables_up_to_n(n)


if __name__ == "__main__":
    main()