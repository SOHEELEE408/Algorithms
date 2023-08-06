import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
end = False
A = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

def dfs(n, depth):
    global end
    if depth == 5:
        end = True
        return
    visited[n] = 1

    for i in A[n]:
        if visited[i] == 0:
            dfs(i, depth+1)
    visited[n] = 0

for i in range(N):
    dfs(i, 1)
    if end:
        break

if end: print(1)
else: print(0)