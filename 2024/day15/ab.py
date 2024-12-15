from itertools import chain
from collections import deque

initial_grid, moves = open(0).read().split('\n\n')
initial_grid = [list(row) for row in initial_grid.split('\n')]
moves = ''.join(moves.split('\n'))

wide_box_chars = ['[', ']']
box_chars = ['O', *wide_box_chars]

directions = {
    'v': (1, 0),
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
}


def expand_grid(grid):
    mapping = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.',
    }

    return [
        list(chain.from_iterable(mapping[cell] for cell in row))
        for row in grid
    ]


def find_connected_boxes(grid, sr, sc, dr, dc):
    boxes = []

    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()

        if grid[r][c] not in box_chars:
            continue

        # Pushing wide boxes vertically can recursively push multiple boxes
        if grid[r][c] in wide_box_chars and dr != 0:
            box_complement_dc = 1 if grid[r][c] == '[' else -1

            for coord in [(r, c), (r, c + box_complement_dc)]:
                if coord not in boxes:
                    boxes.append(coord)

            q.append((r + dr, c))
            q.append((r + dr, c + box_complement_dc))
        else:
            boxes.append((r, c))
            q.append((r + dr, c + dc))

    return boxes


def can_push_boxes(grid, boxes, dr, dc):
    return all(
        (nr, nc) in boxes or grid[nr][nc] == '.'
        for nr, nc in [
            (r + dr, c + dc)
            for r, c in boxes
        ]
    )


def push_boxes(grid, boxes, dr, dc):
    for r, c in reversed(boxes):
        nr, nc = r + dr, c + dc
        grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]


def perform_moves(grid):
    rows = len(grid)
    cols = len(grid[0])

    rr, rc = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '@')
    grid[rr][rc] = '.'

    for move in moves:
        dr, dc = directions[move]
        nr, nc = rr + dr, rc + dc

        if grid[nr][nc] in box_chars:
            connected_boxes = find_connected_boxes(grid, nr, nc, dr, dc)

            if can_push_boxes(grid, connected_boxes, dr, dc):
                push_boxes(grid, connected_boxes, dr, dc)

        if grid[nr][nc] == '.':
            rr, rc = nr, nc

    return sum(
        r * 100 + c
        for r in range(rows)
        for c in range(cols)
        if grid[r][c] in ['[', 'O']
    )


part1_grid = initial_grid
part2_grid = expand_grid(initial_grid)

print(perform_moves(part1_grid))
print(perform_moves(part2_grid))
