import re
from collections import deque

data = open(0).read()
reg_a, reg_b, reg_c, *program = map(int, re.findall(r"-?\d+", data))


def combo(operand, registers):
    assert 0 <= operand < 7
    return operand if operand <= 3 else registers[operand - 4]


def run_program(registers):
    output = []
    ptr = 0

    while ptr < len(program) - 1:
        opcode, operand = program[ptr:ptr + 2]

        match opcode:
            case 0:
                registers[0] = registers[0] // 2 ** combo(operand, registers)
            case 1:
                registers[1] = registers[1] ^ operand
            case 2:
                registers[1] = combo(operand, registers) % 8
            case 3:
                if registers[0] != 0:
                    ptr = operand
                    continue
            case 4:
                registers[1] = registers[1] ^ registers[2]
            case 5:
                output.append(combo(operand, registers) % 8)
            case 6:
                registers[1] = registers[0] // 2 ** combo(operand, registers)
            case 7:
                registers[2] = registers[0] // 2 ** combo(operand, registers)

        ptr += 2

    return output


def lowest_quine_register():
    q = deque([(0, 1)])

    while q:
        previous_candidate, offset = q.popleft()

        for offset_candidate in range(8):
            candidate = previous_candidate * 8 + offset_candidate

            # Values for register B and C are strictly derived from A, thus initial values do not matter
            if run_program([candidate, 0, 0]) == program[-offset:]:
                if offset == len(program):
                    return candidate

                q.append((candidate, offset + 1))


print(','.join(map(str, run_program([reg_a, reg_b, reg_c]))))
print(lowest_quine_register())
