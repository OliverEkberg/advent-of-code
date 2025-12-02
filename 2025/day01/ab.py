lines = [line.strip() for line in open(0)]

a = 0
b = 0

dial = 50

for line in lines:
  distance = int(line[1:])
  whole_turns = distance // 100
  remainder = distance % 100

  prev_dial = dial
  if line.startswith('L'):
    dial = dial - remainder

    if dial < 0 and prev_dial != 0:
      b += 1
  elif line.startswith('R'):
    dial = dial + remainder

    if dial > 100 and prev_dial != 0:
      b += 1

  dial = dial % 100

  b += whole_turns
  if dial == 0:
    a += 1
    b += 1

print(a)
print(b)
