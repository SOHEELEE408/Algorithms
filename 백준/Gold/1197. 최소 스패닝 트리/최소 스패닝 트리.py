import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
Q = PriorityQueue()
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    S, E, W = map(int, input().split())
    Q.put((W, S, E)) # 첫 인자를 기준으로 정렬되므로 가중치를 가장 앞쪽에 저장

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 부모 노드를 업데이트 함으로써 경로 압축
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N-1:
    w, s, e = Q.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)
