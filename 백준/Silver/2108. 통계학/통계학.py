import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

avg = round(sum(nums) / N)

nums.sort()
median = nums[N // 2]

count = Counter(nums)

mode_candidates = count.most_common()
max_freq = mode_candidates[0][1]
modes = [num for num, freq in mode_candidates if freq == max_freq]
modes.sort()
mode = modes[1] if len(modes) > 1 else modes[0]


range_val = nums[-1] - nums[0]

print(avg)
print(median)
print(mode)
print(range_val)
