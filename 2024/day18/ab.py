import re
from itertools import batched
import networkx as nx

data = open(0).read()
numbers = map(int, re.findall(r"-?\d+", data))

# rows, simulate_a = 7, 12
rows, simulate_a = 71, 1024

cols = rows
er, ec = rows - 1, cols - 1


def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols


directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

G = nx.DiGraph()

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if not in_bounds(nr, nc):
                continue

            G.add_edge((r, c), (nr, nc))

simulated = 0
for c, r in batched(numbers, 2):
    if simulated == simulate_a:
        print(nx.shortest_path_length(G, (0, 0), (er, ec)))

    G.remove_node((r, c))
    if not nx.has_path(G, (0, 0), (er, ec)):
        print(f'{c},{r}')
        break

    simulated += 1
