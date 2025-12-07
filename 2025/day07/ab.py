from collections import defaultdict

grid = [list(line.strip()) for line in open(0)]
rows = len(grid)

n_beams = defaultdict(int)

for c, cell in enumerate(grid[0]):
  if cell == 'S':
    n_beams[(0, c)] = 1
    grid[0][c] = '|'

a = 0

for r in range(1, len(grid)):
  for c in range(len(grid[r])):
    if grid[r-1][c] != '|':
      continue

    incoming_beams = n_beams[(r-1, c)]

    if grid[r][c] == '^':
      a += 1
      grid[r][c-1] = '|'
      grid[r][c+1] = '|'
      n_beams[(r, c-1)] += incoming_beams
      n_beams[(r, c+1)] += incoming_beams
    else:
      grid[r][c] = '|'
      n_beams[(r, c)] += incoming_beams

print(a)
print(sum(v for k,v in n_beams.items() if k[0] == rows - 1))
