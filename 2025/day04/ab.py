grid = [list(line.strip()) for line in open(0)]

rows = len(grid)
cols = len(grid[0])

grid_map = {
  (r, c): grid[r][c]
  for r in range(0, rows)
  for c in range(0, cols)
}

dirs = [
  (dr, dc) 
  for dr in range(-1, 2) 
  for dc in range(-1, 2) 
  if (dr, dc) != (0, 0)
]

def can_be_accessed():
  for (r, c), cell in grid_map.items():
    if cell != '@':
      continue

    num_adj = sum(
      1 if grid_map.get((r + dr, c + dc)) == '@' else 0
      for dr, dc in dirs
    )

    if num_adj < 4:
      yield (r, c)

a = None
b = 0

while True:
  accessible = list(can_be_accessed())
  num_accessible = len(accessible)

  b += num_accessible
  if a is None:
    a = num_accessible

  if num_accessible == 0:
    break

  for (r, c) in accessible:
    grid_map[(r, c)] = '.'

print(a)
print(b)
