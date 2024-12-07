from itertools import batched

lines = [line.strip() for line in open(0)]


def priority(groups):
    item_type = next(iter(set.intersection(*map(set, groups))))

    if item_type.islower():
        return ord(item_type) - ord('a') + 1
    else:
        return ord(item_type) - ord('A') + 27


a = sum(priority(batched(line, len(line) // 2)) for line in lines)
b = sum(priority(chunk) for chunk in batched(lines, 3))

print(a)
print(b)
