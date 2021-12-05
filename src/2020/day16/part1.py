#!/usr/bin/env python3

import re


class TicketFieldRules:
    def __init__(self, field, lower_a, upper_a, lower_b, upper_b):
        self.field = field
        self.lower_a = int(lower_a)
        self.upper_a = int(upper_a)
        self.lower_b = int(lower_b)
        self.upper_b = int(upper_b)
        self.valid_numbers = self.compute_valid_numbers()

    def compute_valid_numbers(self):
        valid_numbers = set()
        for i in range(self.lower_a, self.upper_a+1):
            valid_numbers.add(i)
        for j in range(self.lower_b, self.upper_b+1):
            valid_numbers.add(j)
        return valid_numbers


def ticket_scanning(lines):
    your_ticket, nearby_tickets, rules = parse(lines)
    valid_numbers = set()
    invalid_sum = 0
    for rule in rules:
        for i in rule.valid_numbers:
            valid_numbers.add(i)
    for nearby_ticket in nearby_tickets:
        for ticket_id in nearby_ticket:
            if ticket_id not in valid_numbers:
                invalid_sum += ticket_id
    return invalid_sum


def parse(lines):
    i = 0
    your_ticket, nearby_tickets, rules = [], [], []
    while i < len(lines):
        current_line = lines[i]
        if not current_line:
            i += 1
            continue
        if 'your ticket' in current_line:
            # next line is the ticket
            your_ticket = list(map(int,lines[i+1].split(',')))
            i += 3
        elif 'nearby tickets' in current_line:
            for line in lines[i+1:]:
                nearby_tickets.append(list(map(int, line.split(','))))
            break
        else:
            field, lower_a, upper_a, lower_b, upper_b = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)$', current_line).groups()
            rules.append(TicketFieldRules(field, lower_a, upper_a, lower_b, upper_b))
            i += 1
    return your_ticket, nearby_tickets, rules


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(ticket_scanning(lines)))