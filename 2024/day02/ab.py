import itertools

lines = [line.strip() for line in open(0)]


def safe(rapport):
    delta = [rapport[i] - rapport[i + 1] for i in range(len(rapport) - 1)]
    if any(abs(d) > 3 for d in delta):
        return False

    return all(d > 0 for d in delta) or all(d < 0 for d in delta)


rapports = [[int(x) for x in line.split()] for line in lines]

print(sum(safe(r) for r in rapports))
print(sum(any(safe(c) for c in itertools.combinations(r, len(r) - 1)) for r in rapports))
