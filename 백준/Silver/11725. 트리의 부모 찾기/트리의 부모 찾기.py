import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(node):
    visited[node] = True
    for sub in graph[node]:
        if not visited[sub]:
            parents[sub] = node
            dfs(sub)

dfs(1)
for _ in range(2, N+1):
    print(parents[_])

