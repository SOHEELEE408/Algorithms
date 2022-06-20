#2565 전깃줄
import sys

n = int(sys.stdin.readline())
cords = [[0,0] for _ in range(n)]
counts = [0 for _ in range(n)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    cords[_][0] = x
    cords[_][1] = y

cords.sort(key=lambda x:x[0])
"""
for cord1 in cords:
    cnt = 0
    for cord2 in cords:
        if cord2[0] == cord1[0]:
            continue
        elif (cord2[0] > cord1[0] and cord2[1] < cord1[1]) or (cord2[0] < cord1[0] and cord2[1] > cord1[1]):
            cnt += 1
    counts.append(cnt)
"""

for i in range(n):
    for j in range(i):
        if cords[i][1] > cords[j][1] and counts[i] < counts[j]:
            counts[i] = counts[j]
    counts[i] += 1

print(n-max(counts))