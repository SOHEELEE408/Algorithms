import sys

input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()

result = [0] * len(times)
result[0] = times[0]

total = 0

for i in range(1, n):
    result[i] = result[i-1]+times[i]

for _ in result:
    total += _

print(total)