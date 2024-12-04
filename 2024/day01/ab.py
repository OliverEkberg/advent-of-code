from collections import Counter

lines = [line.strip() for line in open(0)]

left = []
right = []
for line in lines:
    l_id, r_id = map(int, line.split())
    left.append(l_id)
    right.append(r_id)

left.sort()
right.sort()

right_counter = Counter(right)

a = sum(abs(l_id - r_id) for l_id, r_id in zip(left, right))
b = sum(l_id * right_counter.get(l_id, 0) for l_id in left)

print(a)
print(b)
