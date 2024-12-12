grid = [list(line.strip()) for line in open(0)]

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


def flood_fill(r, c, component):
    if (r, c) in component:
        return
    component.add((r, c))

    plant_type = grid[r][c]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if not in_bounds(nr, nc) or grid[nr][nc] != plant_type:
            continue

        flood_fill(nr, nc, component)


def get_connected_components():
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if (r, c) in visited:
                continue

            component = set()
            flood_fill(r, c, component)

            visited |= component
            yield component


def get_perimeter(component):
    perimeter = set()

    for r, c in component:
        plant_type = grid[r][c]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if not in_bounds(nr, nc) or grid[nr][nc] != plant_type:
                perimeter.add((r, c, dr, dc))

    return perimeter


def num_perimeter_sides(perimeter):
    perimeter = perimeter.copy()

    q = list(perimeter)
    while q:
        perimeter_part = q.pop()
        if perimeter_part not in perimeter:
            continue

        r, c, dr, dc = perimeter_part
        plant_type = grid[r][c]

        # Walk perimeter by trying all directions
        for ndr, ndc in directions:
            nr = r
            nc = c

            while True:
                nr += ndr
                nc += ndc

                if not in_bounds(nr, nc) or grid[nr][nc] != plant_type:
                    break

                adj_perimeter = (nr, nc, dr, dc)
                if adj_perimeter not in perimeter:
                    break

                perimeter.remove(adj_perimeter)

    return len(perimeter)


a = 0
b = 0

for component in get_connected_components():
    perimeter = get_perimeter(component)

    a += len(component) * len(perimeter)
    b += len(component) * num_perimeter_sides(perimeter)

print(a)
print(b)
