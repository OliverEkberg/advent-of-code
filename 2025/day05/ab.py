fresh_ranges, i_ids = open(0).read().split('\n\n')
fresh_ranges = [
  tuple(map(int, str_range.split('-'))) 
  for str_range in fresh_ranges.split()
]
i_ids = list(map(int, i_ids.split()))

def merge_intervals(intervals):
  sorted_intervals = sorted(intervals, key=lambda x: x[0])
  merged_intervals = []
  
  for l,h in sorted_intervals:
    if not merged_intervals:
      merged_intervals.append((l,h))
      continue
    if l <= merged_intervals[-1][1]:
      merged_intervals[-1] = (
        merged_intervals[-1][0], 
        max(merged_intervals[-1][1], h)
      )
    else:
      merged_intervals.append((l,h))

  return merged_intervals

merged_ranges = merge_intervals(fresh_ranges)
a = sum(
  1
  for i_id in i_ids
  if any(l <= i_id <= h for l,h in merged_ranges)
)
b = sum(h-l+1 for l,h in merged_ranges)

print(a)
print(b)
