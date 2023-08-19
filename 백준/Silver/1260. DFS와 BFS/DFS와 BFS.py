import sys
from collections import deque

input = sys.stdin.readline
N, E, S = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
resultDfs = []
resultBfs = []

for _ in range(E):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for _ in range(1, N+1):
    graph[_].sort()


def dfs(node):

    if visited[node] != True:
        resultDfs.append(node)
        visited[node] = True

        for _ in graph[node]:
            dfs(_)

def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        n = queue.popleft()
        if visited[n] != True:
            resultBfs.append(n)
            visited[n] = True

            for _ in graph[n]:
                queue.append(_)

dfs(S)
visited = [False for _ in range(N+1)]
bfs(S)

for _ in range(len(resultDfs)):
    if _ == len(resultDfs)-1:
        print(resultDfs[_])
    else:
        print(resultDfs[_], end=' ')

for _ in range(len(resultBfs)):
    if _ == len(resultBfs)-1:
        print(resultBfs[_])
    else:
        print(resultBfs[_], end=' ')