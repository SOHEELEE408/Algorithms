import sys

input = sys.stdin.readline
N = int(input())
apartments = [ [] for _ in range(N) ]
total = []
count = 0

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

for _ in range(N):
    part = list(input())
    part.pop()
    apartments[_] = part

def dfs(start):
    global count

    if start[0]<0 or start[0]>=N or start[1]<0 or start[1]>=N:
        return False

    if apartments[start[0]][start[1]] == '1':
        count += 1
        apartments[start[0]][start[1]] = '0'

        for d in direction:
            startX = start[0] + d[0]
            startY = start[1] + d[1]
            dfs([startX, startY])
        return True
    return False

for i in range(N):
    for j in range(N):
        if dfs([i, j]) == True:
            total.append(count)
            count = 0

total.sort()
print(len(total))

for _ in total:
    print(_)