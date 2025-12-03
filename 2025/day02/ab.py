import re

ranges = [tuple(map(int, range.split('-'))) for range in open(0).read().strip().split(',')]

a = 0
b = 0

for r1, r2 in ranges:
  for nbr in range(r1, r2 + 1):
    s_nbr = str(nbr)
    if re.match(r'^(.+?)\1$', s_nbr) is not None:
      a += nbr
    
    if re.match(r'^(.+?)\1+$', s_nbr) is not None:
      b += nbr

print(a)
print(b)
