import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0

for _ in range(n):
    i = 0
    j = n-1
    while i < j:
        temp = nums[i]+nums[j]
        if temp == nums[_]:
            if i != _ and j != _:
                cnt += 1
                break
            elif i == _ :
                i += 1
            elif j == _ :
                j -= 1
        elif temp < nums[_]:
            i += 1
        else :
            j -= 1

print(cnt)