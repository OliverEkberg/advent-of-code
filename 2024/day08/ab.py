from collections import defaultdict
from itertools import combinations

lines = [line.strip() for line in open(0)]

rows = len(lines)
cols = len(lines[0])


def yield_points_on_line(r, c, dr, dc, include_source, max_line_len):
    nr, nc = r, c

    if include_source:
        yield nr, nc

    line_len = 0
    while line_len < max_line_len:
        nr += dr
        nc += dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            break

        yield nr, nc
        line_len += 1


freq_antinodes_map = defaultdict(list)

for r in range(rows):
    for c in range(cols):
        freq = lines[r][c]
        if freq != '.':
            freq_antinodes_map[freq].append((r, c))


def get_antinodes(infinite_lines):
    antinodes = set()

    for freq_antinodes in freq_antinodes_map.values():
        for a1, a2 in combinations(freq_antinodes, 2):
            r1, c1 = a1
            r2, c2 = a2

            dr = r2 - r1
            dc = c2 - c1

            max_line_len = float('inf') if infinite_lines else 1
            antinodes.update(yield_points_on_line(
                r1, c1, -dr, -dc,
                include_source=infinite_lines,
                max_line_len=max_line_len,
            ))
            antinodes.update(yield_points_on_line(
                r2, c2, dr, dc,
                include_source=infinite_lines,
                max_line_len=max_line_len,
            ))

    return antinodes


print(len(get_antinodes(infinite_lines=False)))
print(len(get_antinodes(infinite_lines=True)))
