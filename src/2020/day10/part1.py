#!/usr/bin/env python3

def jolt_differences(lines):
    lines.sort()
    # lines[0] to attach to the charging outlet
    diffs = [lines[0]]
    diffs.extend([num - lines[i] for i, num in enumerate(lines[1:])])
    # 3 because your device's built-in adapter is always 3 higher than the highest adapter
    diffs.append(3)
    return diffs.count(1) * diffs.count(3)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [int(line.strip()) for line in file.readlines()]
        print('Result: ' + str(jolt_differences(lines)))
