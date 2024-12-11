from collections import Counter, defaultdict

stones = list(map(int, open(0).read().split()))

initial_stones = Counter(stones)


def game_of_life(generations):
    stones_map = initial_stones

    for _ in range(generations):
        new_stones_map = defaultdict(int)

        for s_nbr, n in stones_map.items():
            if s_nbr == 0:
                new_stones_map[1] += n
            elif len(str(s_nbr)) % 2 == 0:
                s_nbr_str = str(s_nbr)
                middle = len(s_nbr_str) // 2
                new_stones_map[int(s_nbr_str[:middle])] += n
                new_stones_map[int(s_nbr_str[middle:])] += n
            else:
                new_stones_map[s_nbr * 2024] += n

        stones_map = new_stones_map

    return sum(stones_map.values())


print(game_of_life(25))
print(game_of_life(75))
