#2156 포도주
import sys

n = int(sys.stdin.readline())

total = [0 for _ in range(n+1)]
wine = [0]

for _ in range(n):
    wine.append(int(sys.stdin.readline()))

if n == 1:
    print(wine[1])
else:
    total[1] = wine[1]
    total[2] = wine[1] + wine[2]

    for i in range(3, n+1):
        total[i] = max(total[i-3]+wine[i-1]+wine[i], total[i-2]+wine[i], total[i-1])

    print(max(total))