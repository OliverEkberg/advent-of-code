import networkx as nx

grid = [list(line.strip()) for line in open(0)]


def rotate_clockwise(dr, dc):
    return dc, -dr


def rotate_counter_clockwise(dr, dc):
    return -dc, dr


directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

ROTATE = 1000
MOVE = 1

rows = len(grid)
cols = len(grid[0])

sr, sc = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S')
er, ec = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'E')

G = nx.DiGraph()

G.add_nodes_from([
    (r, c, dr, dc)
    for r in range(rows)
    for c in range(cols)
    if grid[r][c] != '#'
    for dr, dc in directions
])

for r, c, cdr, cdc in G.nodes:
    moves = [
        (cdr, cdc, MOVE),
        (*rotate_clockwise(cdr, cdc), ROTATE + MOVE),
        (*rotate_counter_clockwise(cdr, cdc), ROTATE + MOVE),
    ]

    for dr, dc, cost in moves:
        nr = r + dr
        nc = c + dc

        if (nr, nc, dr, dc) in G.nodes:
            G.add_edge((r, c, cdr, cdc), (nr, nc, dr, dc), weight=cost)

# To avoid having to look for all in-directions for target
for dr, dc in directions:
    G.add_edge((er, ec, dr, dc), (er, ec), weight=0)

print(nx.shortest_path_length(G, (sr, sc, 0, 1), (er, ec), weight="weight"))

print(len({
    (r, c)
    for path in nx.all_shortest_paths(G, (sr, sc, 0, 1), (er, ec), weight="weight")
    for r, c, *_ in path
}))
