grid = [list(map(int, line.strip())) for line in open(0)]

rows = len(grid)
cols = len(grid[0])


def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols


directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def dfs(r, c, peaks):
    if grid[r][c] == 9:
        peaks.add((r, c))
        return 1

    paths_to_peaks = 0
    for dr, dc in directions:
        nr = dr + r
        nc = dc + c

        if not in_bounds(nr, nc) or grid[nr][nc] != grid[r][c] + 1:
            continue

        paths_to_peaks += dfs(nr, nc, peaks)

    return paths_to_peaks


a = 0
b = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            peaks = set()
            b += dfs(r, c, peaks)
            a += len(peaks)

print(a)
print(b)
