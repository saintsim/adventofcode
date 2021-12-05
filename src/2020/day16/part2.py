#!/usr/bin/env python3

from src.day16.part1 import parse


def find_ticket_fields(lines):
    your_ticket, nearby_tickets, rules = parse(lines)
    valid_tickets = get_valid_tickets(rules, nearby_tickets)
    ticket_fields = dict()
    valid_tickets.append(your_ticket)
    for ticket in valid_tickets:
        for x, val in enumerate(ticket):
            suitable_fields = set()
            for rule in rules:
                if val in rule.valid_numbers:
                    suitable_fields.add(rule.field)
            ticket_fields[x] = suitable_fields.intersection(ticket_fields[x]) if x in ticket_fields else suitable_fields
    ticket_fields_final = reduce_options(ticket_fields)
    total = 1
    for i in ticket_fields_final:
        if 'departure' in ticket_fields_final[i]:
            total *= your_ticket[i]
    return total


def reduce_options(ticket_fields):
    ticket_fields_final = dict()
    ticket_fields_final_set = set()
    while len(ticket_fields_final) < len(ticket_fields):
        for i in ticket_fields:
            field_options = ticket_fields[i]
            if not len(field_options):
                continue
            if len(field_options) == 1:
                last_field = field_options.pop()
                ticket_fields_final[i] = last_field
                ticket_fields_final_set.add(last_field)
            else:
                ticket_fields[i] = field_options - ticket_fields_final_set
    return ticket_fields_final


def get_valid_tickets(rules, nearby_tickets):
    valid_numbers = set()
    for rule in rules:
        for i in rule.valid_numbers:
            valid_numbers.add(i)
    valid_tickets = []
    for nearby_ticket in nearby_tickets:
        valid = True
        for ticket_id in nearby_ticket:
            if ticket_id not in valid_numbers:
                valid = False
                break
        if valid:
            valid_tickets.append(nearby_ticket)
    return valid_tickets


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(find_ticket_fields(lines)))
