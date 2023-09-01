import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
delete = int(input())

graph = [[] for _ in range(N)]
visited = [False] * N
leaf = []
root = 0

for _ in range(N):
    parent = parents[_]
    if parents[_] != -1:
        graph[parent].append(_)
    else:
        root = _

def dfs(node):
    visited[node] = True
    subCnt = 0

    if node != delete:
        for sub in graph[node]:
            if not visited[sub] and sub != delete:
                subCnt += 1
                dfs(sub)
        if subCnt == 0:
            leaf.append(node)

dfs(root)
print(len(leaf))