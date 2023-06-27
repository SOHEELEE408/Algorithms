import copy
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
D = [60000001] * (N+1)
D[1]=0
graph = []

for _ in range(M):
    abc = list(map(int, input().split()))
    graph.append(abc)

for _ in range(N-1):
    for edge in graph:
        start = edge[0]
        end = edge[1]
        distance = edge[2]

        if D[start] > 60000000:
            continue
        D[end] = min(D[end], D[start]+distance)

checkD = copy.deepcopy(D)

for edge in graph:
    start = edge[0]
    end = edge[1]
    distance = edge[2]

    if D[start] > 60000000:
        continue
    D[end] = min(D[end], D[start]+distance)

if checkD != D:
    print(-1)
else:
    for _ in range(2, N+1):
        if D[_] > 60000000:
            print(-1)
        else:
            print(D[_])
