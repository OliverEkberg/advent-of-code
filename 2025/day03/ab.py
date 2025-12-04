lines = [line.strip() for line in open(0)]

def _joltage(s, n):
  if n == 0:
    return []

  if n == 1:
    return [max(s)]

  b = max(s[:-n+1])
  return [b] + _joltage(s[s.index(b) + 1:], n - 1)

def joltage(s, n):
  return int(''.join(_joltage(s, n)))

a = sum(joltage(line, 2) for line in lines)
b = sum(joltage(line, 12) for line in lines)

print(a)
print(b)
