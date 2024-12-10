SAFE = 1
UNSAFE = 0


def is_safe(levels):
    # Check if levels are either strictly increasing or strictly decreasing
    increasing = all(levels[i + 1] > levels[i] for i in range(len(levels) - 1))
    decreasing = all(levels[i + 1] < levels[i] for i in range(len(levels) - 1))

    # Check if differences between adjacent levels are between 1 and 3
    for i in range(len(levels) - 1):
        diff = abs(levels[i + 1] - levels[i])
        if diff < 1 or diff > 3:
            return UNSAFE

    # If either increasing or decreasing, it's safe
    if increasing or decreasing:
        return SAFE
    return UNSAFE


def part2(input_data):
    safe_count = 0

    for line in input_data.split('\n'):
        if not line.strip():
            continue  # Skip empty lines

        levels = list(map(int, line.split()))

        # First check if the report is already safe
        if is_safe(levels) == SAFE:
            safe_count += 1
            print(levels)
        else:
            # Check if removing one level results in a safe report
            report_safe = False
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i + 1:]  # Remove one level
                if is_safe(modified_levels) == SAFE:
                    report_safe = True
                    break

            if report_safe:
                safe_count += 1
                print(levels)

    return safe_count


if __name__ == '__main__':
    with open('input', 'r') as file:
        input_data = file.read()
        result = part2(input_data)
        print('Result:', result)