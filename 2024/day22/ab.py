from collections import defaultdict

secrets = [int(line.strip()) for line in open(0)]


def mix_and_prune(old_secret, new_secret):
    return (new_secret ^ old_secret) % 16777216


def evolve(secret):
    secret = mix_and_prune(secret, secret * 64)
    secret = mix_and_prune(secret, secret // 32)
    secret = mix_and_prune(secret, secret * 2048)
    return secret


def get_price(secret):
    return int(str(secret)[-1])


CONSECUTIVE_CHANGES = 4
aggregated_pattern_to_price = defaultdict(int)
a = 0

for secret in secrets:
    price_deltas = []
    pattern_to_price = {}

    for _ in range(2000):
        prev_price = get_price(secret)
        secret = evolve(secret)
        new_price = get_price(secret)

        price_deltas.append(new_price - prev_price)

        if len(price_deltas) >= CONSECUTIVE_CHANGES:
            pattern = tuple(price_deltas[-CONSECUTIVE_CHANGES:])

            if pattern not in pattern_to_price:
                pattern_to_price[pattern] = new_price

    for pattern, price in pattern_to_price.items():
        aggregated_pattern_to_price[pattern] += price

    a += secret

print(a)
print(max(aggregated_pattern_to_price.values()))
