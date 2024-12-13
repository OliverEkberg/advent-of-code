from z3 import Solver, Int, sat

equations = [list(chunk.split('\n')) for chunk in open(0).read().strip().split('\n\n')]


def tokens_required(px, py, ax, ay, bx, by):
    solver = Solver()

    a = Int('a')
    b = Int('b')

    solver.add(a * ax + b * bx == px)
    solver.add(a * ay + b * by == py)

    if solver.check() != sat:
        return 0

    return solver.model()[a].as_long() * 3 + solver.model()[b].as_long()


a = 0
b = 0

for equation in equations:
    button_a, button_b, prize = equation
    ax, ay = [int(v.split('+')[1]) for v in button_a.split(': ')[1].split(', ')]
    bx, by = [int(v.split('+')[1]) for v in button_b.split(': ')[1].split(', ')]
    px, py = [int(v.split('=')[1]) for v in prize.split(': ')[1].split(', ')]

    a += tokens_required(px, py, ax, ay, bx, by)
    b += tokens_required(px + 10000000000000, py + 10000000000000, ax, ay, bx, by)

print(a)
print(b)
