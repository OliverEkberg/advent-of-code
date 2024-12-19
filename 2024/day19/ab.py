from functools import cache

data = open(0).read()
available, desired = data.split('\n\n')
available = set(available.split(', '))
desired = list(desired.split())


@cache
def different_ways(partial_pattern):
    ways = 0

    if partial_pattern in available:
        ways += 1

    for i in range(1, len(partial_pattern)):
        if partial_pattern[:i] in available:
            ways += different_ways(partial_pattern[i:])

    return ways


print(sum(different_ways(d) > 0 for d in desired))
print(sum(different_ways(d) for d in desired))
