#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import namedtuple
import queue

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, level, value, weight, taken):
        self.level = level
        self.value = value
        self.weight = weight
        self.taken = taken

    def __lt__(self, other):
        return (self.value < other.value)

def upper_bound(node, items, capacity):
    upper_bound_value = node.value
    upper_bound_weight = node.weight
    current_level = node.level

    while current_level < len(items) and upper_bound_weight + items[current_level].weight <= capacity:
        upper_bound_value += items[current_level].value
        upper_bound_weight += items[current_level].weight
        current_level += 1

    if current_level < len(items):
        remaining_capacity = capacity - upper_bound_weight
        upper_bound_value += items[current_level].value * (remaining_capacity / items[current_level].weight)

    return upper_bound_value

def branch_and_bound(items, capacity):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    best_solution = [0] * len(items)
    best_value = 0

    q = queue.PriorityQueue()
    root_node = Node(0, 0, 0, [])
    q.put((-upper_bound(root_node, items, capacity), root_node))

    while not q.empty():
        _, node = q.get()

        if node.level == len(items):
            if node.value > best_value:
                best_value = node.value
                best_solution = node.taken
            continue

        next_item = items[node.level]

        # Explore without including the item
        exclude_node = Node(
            node.level + 1,
            node.value,
            node.weight,
            node.taken + [0]
        )
        exclude_bound = upper_bound(exclude_node, items, capacity)
        if exclude_bound > best_value:
            q.put((-exclude_bound, exclude_node))

        # Explore including the item
        if node.weight + next_item.weight <= capacity:
            include_node = Node(
                node.level + 1,
                node.value + next_item.value,
                node.weight + next_item.weight,
                node.taken + [1]
            )
            include_bound = upper_bound(include_node, items, capacity)
            if include_bound > best_value:
                q.put((-include_bound, include_node))

    return best_solution, best_value

def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # Run branch and bound algorithm
    taken, value = branch_and_bound(items, capacity)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
