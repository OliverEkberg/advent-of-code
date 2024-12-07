ordered_inventories = sorted(sum(map(int, chunk.split())) for chunk in open(0).read().split('\n\n'))

print(ordered_inventories[-1])
print(sum(ordered_inventories[-3:]))
