from operator import add, mul

lines = [line.strip() for line in open(0)]


def concat_digits(a, b):
    return int(str(a) + str(b))


def can_solve(operators, operands, operand_idx, current_value, target_value):
    if operand_idx == len(operands):
        return current_value == target_value

    return any(
        can_solve(
            operators,
            operands,
            operand_idx + 1,
            operator(current_value, operands[operand_idx]),
            target_value,
        )
        for operator in operators
    )


def total_calibration(equations, operators):
    return sum(
        target for target, operands in equations
        if can_solve(operators, operands, 1, operands[0], target)
    )


equations = []
for line in lines:
    target, *operands = map(int, line.replace(': ', ' ').split())
    equations.append((target, operands))

print(total_calibration(equations, [add, mul]))
print(total_calibration(equations, [add, mul, concat_digits]))
