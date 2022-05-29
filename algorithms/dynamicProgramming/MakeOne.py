#1463번 1로 만들기
import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
nums = [0 for _ in range(n+1)]
"""
nums[1] = 1
nums[2] = 1
nums[3] = 1

def dp(x):
    if nums[x] != 0:
        return nums[x]
    else:
        if x=%3 = 0:
            nums[x] = min(dp(int(x/3)), dp(int(x-1))) + 1
        elif x%2 == 0:
            nums[x] = min(dp(int(x/2)), dp(int(x-1))) + 1
        else:
            nums[x] = dp(x-1) + 1
        return nums[x]

print(dp(n))
"""

for i in range(2, n+1):
    nums[i] = nums[i-1]+1
    if i%3 == 0:
        nums[i] = nums[int(i/3)]+1 if nums[int(i/3)]<nums[i] else nums[i]
    if i%2 == 0:
        nums[i] = nums[int(i/2)]+1 if nums[int(i/2)]<nums[i] else nums[i]

print(nums[n])