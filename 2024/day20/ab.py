grid = [list(line.strip()) for line in open(0)]

rows = len(grid)
cols = len(grid[0])

sr, sc = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S')
er, ec = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'E')

walls = {
    (r, c)
    for r in range(rows)
    for c in range(cols)
    if grid[r][c] == '#'
}

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols


nodes = {(er, ec): 0}
r, c = er, ec

while (r, c) != (sr, sc):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if not in_bounds(nr, nc) or (nr, nc) in walls or (nr, nc) in nodes:
            continue

        nodes[(nr, nc)] = nodes[(r, c)] + 1
        r, c = nr, nc


def possible_cheats(r, c, max_cheat_duration):
    for dr in range(-max_cheat_duration, max_cheat_duration + 1):
        for dc in range(-max_cheat_duration, max_cheat_duration + 1):
            if (abs(dr) + abs(dc)) > max_cheat_duration:
                continue

            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and (nr, nc) not in walls:
                yield nr, nc


def good_cheats(max_cheat_duration):
    count = 0

    for r, c in nodes.keys():
        for nr, nc in possible_cheats(r, c, max_cheat_duration):
            cheat_duration = abs(r - nr) + abs(c - nc)
            saving = nodes[(r, c)] - nodes[(nr, nc)] - cheat_duration
            if saving >= 100:
                count += 1

    return count


print(good_cheats(2))
print(good_cheats(20))
