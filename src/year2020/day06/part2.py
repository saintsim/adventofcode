#!/usr/bin/env python3


def size_of_intersection(lists):
    intersection_set = set(lists[0])
    for this_list in lists[1:]:
        intersection_set.intersection_update(this_list)
    return len(intersection_set)


def customs_form_sum(lines):
    total, group = 0, []
    for line in lines:
        person = set()
        if line == "\n":
            total += size_of_intersection(group)
            group = []
        else:
            for token in line.strip():
                person.add(token)
            group.append(person)
    return total + size_of_intersection(group)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(customs_form_sum(file.readlines())))
