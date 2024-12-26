import itertools
from collections import deque
from operator import and_, or_, xor

initial_wire_values, gate_connections = open(0).read().strip().split('\n\n')

wire_values = {}
gates = {}

for x in initial_wire_values.split('\n'):
    wire_id, value = x.split(': ')
    wire_values[wire_id] = int(value)

for x in gate_connections.split('\n'):
    gate_input, gate_output = x.split(' -> ')
    ref1, op, ref2 = gate_input.split()

    gates[frozenset((ref1, op, ref2))] = (ref1, op, ref2, gate_output)


def simulate():
    q = deque(gates.values())

    operators = {
        'AND': and_,
        'OR': or_,
        'XOR': xor,
    }

    while q:
        ref1, op, ref2, output = q.popleft()
        if ref1 not in wire_values or ref2 not in wire_values:
            q.append((ref1, op, ref2, output))
            continue

        wire_values[output] = operators[op](wire_values[ref1], wire_values[ref2])


def z_output():
    z_wires_binary = ''.join(
        str(wire_values[ref])
        for ref in sorted([
            ref for ref in wire_values.keys() if ref.startswith('z')
        ], reverse=True)
    )
    return int(z_wires_binary, 2)


def get_reference(ref1, op, ref2):
    gate = gates.get(frozenset((ref1, op, ref2)))
    return gate[3] if gate else None


def ensure_full_adders():
    swaps = []
    num_bits = sum(ref.startswith('x') for ref in wire_values.keys())

    c_in = None
    for bit in range(num_bits):
        bit = str(bit).zfill(2)

        a1_xor = get_reference(f'x{bit}', 'XOR', f'y{bit}')
        a1_and = get_reference(f'x{bit}', 'AND', f'y{bit}')

        if bit == '00':
            c_in = a1_and
            continue

        a2_and = get_reference(c_in, 'AND', a1_xor)
        if not a2_and:
            a1_and, a1_xor, = a1_xor, a1_and
            swaps += [a1_and, a1_xor]
            a2_and = get_reference(c_in, 'AND', a1_xor)

        a2_xor = get_reference(c_in, 'XOR', a1_xor)

        if a1_xor.startswith('z'):
            a1_xor, a2_xor = a2_xor, a1_xor
            swaps += [a1_xor, a2_xor]

        if a1_and.startswith('z'):
            a1_and, a2_xor = a2_xor, a1_and
            swaps += [a1_and, a2_xor]

        if a2_and.startswith('z'):
            a2_and, a2_xor = a2_xor, a2_and
            swaps += [a2_and, a2_xor]

        c_out = get_reference(a2_and, 'OR', a1_and)

        # Carry will go directly into last bit
        if c_out.startswith('z') and c_out != f'z{num_bits}':
            c_out, a2_xor = a2_xor, c_out
            swaps += [c_out, a2_xor]

        c_in = c_out

    return swaps


simulate()
print(z_output())

swaps = ensure_full_adders()
print(','.join(sorted(swaps)))
