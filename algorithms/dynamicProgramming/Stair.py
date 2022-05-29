#2579 계단 오르기
import sys

n = int(sys.stdin.readline())

total = [0 for _ in range(n+1)]
stair = [0]

for _ in range(n):
    stair.append(int(sys.stdin.readline()))

if n == 1:
    print(stair[1])
else:
    total[1] = stair[1]
    total[2] = stair[1] + stair[2]

    for i in range(3, n+1):
        total[i] = max(total[i-3]+stair[i-1]+stair[i], total[i-2]+stair[i])

    print(total[n])