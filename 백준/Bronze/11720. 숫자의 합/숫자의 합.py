import sys

input = sys.stdin.readline

n = int(input())
nums = list(input())
total = 0

for i in range(n):
    total += int(nums[i])

print(total)