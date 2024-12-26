schematics = open(0).read().strip().split('\n\n')

keys = set()
locks = set()

for schematic in schematics:
    schematic = schematic.split('\n')

    heights = tuple(
        sum(schematic[r][c] == '#' for r in range(len(schematic)))
        for c in range(len(schematic[0]))
    )

    if schematic[0][0] == '#':
        locks.add(heights)
    else:
        keys.add(heights)

max_height = 7
unique_pairs = sum(
    all(hk + hl <= max_height for hk, hl in zip(k, l))
    for k in keys
    for l in locks
)
print(unique_pairs)
