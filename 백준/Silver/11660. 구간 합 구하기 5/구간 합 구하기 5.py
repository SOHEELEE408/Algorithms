import sys

n, m = map(int, sys.stdin.readline().split(" "))

numbers = [[] for _ in range(n+1)] # O(n)
numbers[0] = [0 for _ in range(n+1)] # O(n)
sums = [[0 for _ in range(n+1)] for _ in range(n+1)] # O(n^2)


for _ in range(1, n+1) : # O(n)
    tmp = [0] + list(map(int, sys.stdin.readline().split(" ")))
    numbers[_] = tmp

for i in range(1, n+1) : # O(n^2)
    for j in range(1, n+1) :
        sums[i][j] = sums[i-1][j] + sums[i][j-1] + numbers[i][j] - sums[i-1][j-1]

for _ in range(m) : # O(n)
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(" "))
    print(sums[x2][y2]-sums[x1-1][y2]-sums[x2][y1-1]+sums[x1-1][y1-1])