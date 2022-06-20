import sys

l = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d = [0 for _ in range(l)]
d2 = [0 for _ in range(l)]
result = [0 for _ in range(l)]

for i in range(l):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

for i in range(l-1,-1,-1):
    for j in range(l-1, i, -1):
        if a[i] > a[j] and d2[i]<d2[j]:
            d2[i] = d2[j]
    d2[i] += 1

for i in range(l):
    result[i] = d[i]+d2[i]-1

print(max(result))