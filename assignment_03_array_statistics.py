# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)

def calculate_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def calculate_min(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def get_numbers_from_user():
    while True:
        try:
            n = int(input("Enter the number of elements: "))
        except ValueError:
            print("Please enter a valid integer.")
            return None

        if n <= 0:
            print("Please enter a positive integer.")
            return None

        break

    numbers=[]
    for i in range(1, n + 1):
        while True:
            try:
                value = float(input(f"Enter number {i}"))
                if value == int(value):
                    value = int(value)
                    numbers.append(value)
                    break
            except ValueError:
                print("Please enter a valid number.")

    return numbers

def main():
    numbers = get_numbers_from_user()

    if numbers is None:
        return

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    largest = calculate_max(numbers)
    smallest = calculate_min(numbers)

    print("\nResults:")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {largest}")
    print(f"Minimum: {smallest}")

if __name__ == "__main__":
    main()
