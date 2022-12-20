#!/usr/bin/env python3

NODES = dict()
NODES_SIZE = 0


class Node:

    def __init__(self, val, prev_ptr, next_ptr):
        self.val = val
        self.prev_ptr = prev_ptr
        self.next_ptr = next_ptr
        self.complete = False


def get_node_ptr(i):
    return i % NODES_SIZE


def get_prev(node_id):
    return NODES[get_node_ptr(node_id)].prev_ptr


def get_next(node_id):
    return NODES[get_node_ptr(node_id)].next_ptr


def find_solution(zero_node_id):
    next_ptr = zero_node_id
    total = 0
    for i in range(3001):
        if i == 1000 or i == 2000 or i == 3000:
            print(NODES[next_ptr].val)
            total += NODES[next_ptr].val
        next_ptr = get_next(next_ptr)
    return total


def populate_nodes(input):
    j = 0
    prev_ptr = len(input)-1
    zero_node_id = None
    global NODES_SIZE
    NODES_SIZE = len(input)
    for token in input:
        next_ptr = get_node_ptr(j+1)
        NODES[j] = Node(int(token), prev_ptr, next_ptr)
        prev_ptr = j
        if int(token) == 0:
            zero_node_id = j
        j += 1
    return zero_node_id


def grove(input):
    zero_node_id = populate_nodes(input)
    for i in range(len(input)):
        node_to_move = NODES[i]
        node_to_move_old_prev = node_to_move.prev_ptr
        node_to_move_old_next = node_to_move.next_ptr
        if node_to_move.val < 0:
            # backwards
            node_to_move_new_prev = node_to_move.prev_ptr
            # e.g. 1 | 2 | 3 | 4 | 5 | 6
            #  to move 5 (node_to_move) to between 1 and 2
            #  we need to update 1.next, 2.prev, 4.next, 6.prev,
            #  + 5.prev (node_to_move_new_prev), 5.next (node_to_move_new_next)
            for move_back_idx in range(abs(node_to_move.val)):
                # find which node we are inserting our node_to_move around
                node_to_move_new_prev = get_prev(node_to_move_new_prev)
            # update the old neighbours of the moved one
            NODES[get_node_ptr(node_to_move_old_prev)].next_ptr = node_to_move_old_next
            NODES[get_node_ptr(node_to_move_old_next)].prev_ptr = node_to_move_old_prev
            # need to move re-link
            node_to_move.prev_ptr = node_to_move_new_prev
            node_to_move.next_ptr = get_next(node_to_move_new_prev)
            # update the new neighbours of the moved one
            NODES[get_node_ptr(node_to_move_new_prev)].next_ptr = i
            NODES[get_node_ptr(node_to_move.next_ptr)].prev_ptr = i
        elif node_to_move.val > 0:
            # TODO: clean up the below, thar dupes the backwards in parts
            # forwards
            node_to_move_new_next = node_to_move.next_ptr
            for move_back_idx in range(abs(node_to_move.val)):
                # find which node we are inserting our node_to_move around
                node_to_move_new_next = get_next( node_to_move_new_next)
            # update the old neighbours of the moved one
            NODES[get_node_ptr(node_to_move_old_prev)].next_ptr = node_to_move_old_next
            NODES[get_node_ptr(node_to_move_old_next)].prev_ptr = node_to_move_old_prev
            # need to move re-link
            node_to_move.next_ptr = node_to_move_new_next
            node_to_move.prev_ptr = get_prev(node_to_move_new_next)
            # update the new neighbours of the moved one
            NODES[get_node_ptr(node_to_move_new_next)].prev_ptr = i
            NODES[get_node_ptr(node_to_move.prev_ptr)].next_ptr = i
        node_to_move.complete = True
        i += 1
    return find_solution(zero_node_id)


if __name__ == '__main__':
    with open('example', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(grove(lines)))