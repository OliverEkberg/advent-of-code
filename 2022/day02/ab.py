rounds = [line.strip().split() for line in open(0)]

ROCK, PAPER, SCISSORS = 'A', 'B', 'C'
shape_points = {ROCK: 1, PAPER: 2, SCISSORS: 3}
beats = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
is_beaten_by = {v: k for k, v in beats.items()}


def mapping_a(pair):
    a, b = pair
    return a, {
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSORS
    }[b]


def mapping_b(pair):
    a, b = pair
    return a, {
        'X': beats[a],  # Win
        'Y': a,  # Draw
        'Z': is_beaten_by[a],  # Loose
    }[b]


def score_strategy(strategy):
    points = 0
    for opponent, you in strategy:
        points += shape_points[you]

        if opponent == you:
            points += 3
        elif beats[you] == opponent:
            points += 6

    return points


print(score_strategy(map(mapping_a, rounds)))
print(score_strategy(map(mapping_b, rounds)))
