from functools import cache

lines = [line.strip() for line in open(0)]


def num(s):
    return int(''.join(c for c in s if c.isdigit()))


def sign(n):
    if n == 0:
        return 0
    return 1 if n > 0 else -1


keypad_pos = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2),
}

dpad_pos = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

directions = {
    (1, 0): 'v',
    (-1, 0): '^',
    (0, 1): '>',
    (0, -1): '<',
}


def get_possible_steps(src, target, valid_pos):
    if src == target:
        return {'A'}

    if src not in valid_pos:
        return set()

    sr, sc = src
    tr, tc = target

    possible_steps = set()

    for delta in [(tr - sr, 0), (0, tc - sc)]:
        dr, dc = map(sign, delta)

        if (dr, dc) not in directions:
            continue

        possible_steps |= {
            directions[(dr, dc)] + step
            for step in get_possible_steps(
                (sr + dr, sc + dc), target, valid_pos
            )
        }

    return set(possible_steps)


@cache
def shortest_sequence(steps, robots, current_robot=0):
    pos = keypad_pos if current_robot == 0 else dpad_pos
    src = pos['A']

    sequence_len = 0

    for step in steps:
        target = pos[step]
        possible_steps = get_possible_steps(src, target, set(pos.values()))

        # We are processing the last robot
        if current_robot == robots:
            sequence_len += min(map(len, possible_steps))
        else:
            sequence_len += min(shortest_sequence(ps, robots, current_robot + 1) for ps in possible_steps)

        src = target

    return sequence_len


print(sum(shortest_sequence(line, robots=2) * num(line) for line in lines))
print(sum(shortest_sequence(line, robots=25) * num(line) for line in lines))
