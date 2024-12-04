lines = [line.strip() for line in open(0)]

rows = len(lines)
cols = len(lines[0])

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

a = 0
b = 0

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            word = ''
            nr = r
            nc = c

            for _ in range(4):
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    break

                word += lines[nr][nc]
                nc += dc
                nr += dr

            if word == 'XMAS':
                a += 1

        if lines[r][c] == 'A' and 0 < r < rows - 1 and 0 < c < cols - 1:
            diagonal_1 = lines[r - 1][c - 1] + lines[r + 1][c + 1]
            diagonal_2 = lines[r - 1][c + 1] + lines[r + 1][c - 1]

            accepted = ['MS', 'SM']
            if diagonal_1 in accepted and diagonal_2 in accepted:
                b += 1

print(a)
print(b)
