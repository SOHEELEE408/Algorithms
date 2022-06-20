#11053 가장 긴 증가하는 부분 수열
import sys

l = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [0 for _ in range(l)]

for i in range(l):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))




import sys

N = int(sys.stdin.readline()[:-1])
nums = list(map(int, sys.stdin.readline()[:-1].split()))

dp = [[0, 0] for _ in range(1001)]
dp[0] = [1, 1]

max_length = 1

for i in range(1, N):
    dp[i] = [1, 1]
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        if nums[i] < nums[j]:
            dp[i][1] = max(dp[i][1], max(dp[j]) + 1)
    max_length = max(max_length, dp[i][0], dp[i][1])

print(max_length)