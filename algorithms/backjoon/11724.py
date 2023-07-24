import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
con = [ [] for _ in range(N+1)]
visited = []
total = 0

for _ in range(M):
    u, v = map(int, input().split())
    con[u].append(v)
    con[v].append(u)

def dfs(n):
    visited.append(n)
    for _ in con[n]:
        if _ not in visited:
            dfs(_)

for i in range(1, N+1):
    if i not in visited:
        dfs(i)
        total += 1

print(total)


# 풀이 2

visited = []
total = 0

def dfs_2(n):

    if n not in visited:
        visited.append(n)
        for _ in con[n]:
            dfs(_)
        return True

    return False

for i in range(1, N+1):
    if dfs_2(i) == True:
        total += 1

print(total)








