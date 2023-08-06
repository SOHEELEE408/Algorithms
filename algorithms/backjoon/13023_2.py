import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
friends = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

result = 0

def dfs(a, count, visited = []):
    global result

    if count == 5:
        result = 1
        return

    visited.append(a)
    for b in friends[a]:
        if b not in visited:
            print(visited)
            dfs(b, count + 1, visited)
    #visited.remove(a)

for _ in range(N):
    dfs(_, 1)
    if result == 1:
        break

if result == 1:
    print(1)
else:
    print(0)

# 8 8
# 1 7
# 3 7
# 4 7
# 3 4
# 4 6
# 3 5
# 0 4
# 2 7
# [0]
# [0, 4]
# [0, 4, 7]
# [0, 4, 7]
# [0, 4, 7, 3]
# [0, 4, 7]
# [0, 4]
# [0, 4, 3]
# [0, 4, 3, 7]
# [0, 4, 3, 7]
# [0, 4, 3]
# [0, 4]
# 1
