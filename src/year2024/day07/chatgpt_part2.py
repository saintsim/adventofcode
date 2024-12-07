import itertools


# Function to evaluate an expression with a list of numbers and operators
def evaluate_expression(numbers, operators):
    # Start with the first number
    result = numbers[0]

    # Loop through the rest of the numbers and apply operators from left to right
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]
        elif operators[i - 1] == '*':
            result *= numbers[i]
        elif operators[i - 1] == '||':
            result = int(f"{result}{numbers[i]}")

    return result


# Function to solve the puzzle
def solve_puzzle(input_data):
    total_calibration_result = 0

    # Loop over each line in the input data
    for line in input_data:
        # Split the line into the test value and the list of numbers
        test_value, numbers_str = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers_str.split()))

        # Create a list of all possible operators (+, *, ||)
        operators = ['+', '*', '||']

        # Generate all possible operator combinations for the gaps between numbers
        num_positions = len(numbers) - 1
        if num_positions > 0:
            operator_combinations = itertools.product(operators, repeat=num_positions)

            # Check each operator combination
            for ops in operator_combinations:
                if evaluate_expression(numbers, ops) == test_value:
                    print(line)
                    total_calibration_result += test_value
                    break  # No need to check further combinations for this equation

    return total_calibration_result


# Example input
input_data = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20"
]

if __name__ == '__main__':
    with open('input', 'r') as file:
        # Solve the puzzle
        result = solve_puzzle(file.read().split('\n'))
        print("Total calibration result:", result)