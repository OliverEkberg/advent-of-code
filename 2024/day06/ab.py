from operator import itemgetter

matrix = [list(line.strip()) for line in open(0)]
rows = len(matrix)
cols = len(matrix[0])

sr, sc = next((r, c) for r in range(rows) for c in range(cols) if matrix[r][c] == '^')


def rotate(dr, dc):
    return dc, -dr


def simulate():
    dr, dc = -1, 0
    r, c = sr, sc

    visited = {(r, c, dr, dc)}
    while True:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False, set(map(itemgetter(0, 1), visited))

        if matrix[nr][nc] == '#':
            dr, dc = rotate(dr, dc)
            continue

        r, c = nr, nc
        if (r, c, dr, dc) in visited:
            return True, []

        visited.add((r, c, dr, dc))


_, visited_a = simulate()
print(len(visited_a))

b = 0

for r, c in visited_a:
    if matrix[r][c] != '.':
        continue

    matrix[r][c] = '#'
    contains_loop, _ = simulate()
    matrix[r][c] = '.'

    if contains_loop:
        b += 1

print(b)
