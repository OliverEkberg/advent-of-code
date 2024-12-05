rule_lines, update_lines = [r.split() for r in open(0).read().split('\n\n')]

rules = [tuple(map(int, rule_line.split('|'))) for rule_line in rule_lines]
updates = [list(map(int, update_line.split(','))) for update_line in update_lines]


def rule_passes(update, rule):
    before, after = rule
    return (
            before not in update
            or after not in update
            or update.index(before) < update.index(after)
    )


def enforce_rule(update, rule):
    _, after = rule
    while not rule_passes(update, rule):
        after_idx = update.index(after)
        update[after_idx], update[after_idx + 1] = update[after_idx + 1], update[after_idx]


a = 0
b = 0

for update in updates:
    if all(rule_passes(update, rule) for rule in rules):
        a += update[len(update) // 2]
    else:
        rule_idx = 0

        while rule_idx < len(rules):
            rule = rules[rule_idx]

            if rule_passes(update, rule):
                rule_idx += 1
            else:
                enforce_rule(update, rule)
                rule_idx = 0  # Reprocess all rules

        b += update[len(update) // 2]

print(a)
print(b)
