import math
from re import X

lines = open(0).read().rstrip('\n').split('\n')
column_indexes = [i for i, c in enumerate(lines[-1]) if c != ' ']

grid = [
  [line[c:d] for c, d in zip(column_indexes, column_indexes[1:] + [None])]
  for line in lines
]

rows = len(grid)
cols = len(grid[0])

a = 0
b = 0

for c in range(cols):
  sign = grid[rows - 1][c][0]
  acc = sum if sign == '+' else math.prod
  operands = [grid[r][c] for r in range(rows - 1)]

  a += acc(map(int, operands))

  cell_width = len(operands[0])
  b += acc(
    int(x)
    for x in (
      ''.join(o[j] for o in operands)
      for j in range(cell_width)
    )
    if x.strip() != ''
  )

print(a)
print(b)
