from itertools import batched, count
from math import prod
import re

rows = 103
cols = 101


# Uncomment for test data
# rows = 7
# cols = 11

def count_robots_in_quadrants(robots):
    mr = rows // 2
    mc = cols // 2
    quadrants = {0: 0, 1: 0, 2: 0, 3: 0}

    for r, c, _, _ in robots:
        if r == mr or c == mc:
            continue

        qr = int(r < mr)
        qc = int(c < mc)

        quadrants[qr * 2 + qc] += 1

    return quadrants


data = open(0).read()
numbers = map(int, re.findall(r"-?\d+", data))

robots = [(pr, pc, dr, dc) for pc, pr, dc, dr in batched(numbers, 4)]

for second in count(start=1):
    next_robots = []
    occupied_coords = set()

    for robot in robots:
        r, c, dr, dc = robot

        r = (r + dr) % rows
        c = (c + dc) % cols

        occupied_coords.add((r, c))
        next_robots.append((r, c, dr, dc))

    robots = next_robots

    if second == 100:
        print(prod(count_robots_in_quadrants(robots).values()))

    if len(occupied_coords) == len(robots):
        print(second)
        exit(0)
