import math
import re

lines = [line.strip() for line in open(0)]
program = ''.join(lines)

a = 0
b = 0
enabled = True

for match in re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", program):
    if match == 'do()':
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        result = math.prod(map(int, match[4:-1].split(',')))

        a += result
        if enabled:
            b += result

print(a)
print(b)
