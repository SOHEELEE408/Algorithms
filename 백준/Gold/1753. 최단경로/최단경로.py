import sys
from queue import PriorityQueue

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
D = [ 600001 for _ in range(V+1)]
D[K] = 0
visited = [0] * (V+1)
graph = {}
que = PriorityQueue()

que.put((0, K))

for _ in range(1, V+1):
    graph[_] = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


while que.qsize() > 0:
    current = que.get()[1]

    if visited[current] == 1:
        continue
    visited[current] = 1

    for _ in range(len(graph[current])):
        node = graph[current][_][0]
        w = graph[current][_][1]

        D[node] = min(D[node], D[current]+w)
        que.put((D[node], node))


for _ in range(1, V+1):
    if D[_] > 600000:
        print('INF')
    else:
        print(D[_])