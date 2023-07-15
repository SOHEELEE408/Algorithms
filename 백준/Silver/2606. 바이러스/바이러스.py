import sys

input = sys.stdin.readline
computerCnt = int(input())
edge = int(input())
visitedList = []
connect = [[] for _ in range(computerCnt+1)]

for _ in range(edge):
    computerA, computerB = map(int, input().split())
    connect[computerA].append(computerB)
    connect[computerB].append(computerA)

def dfs(graph, start, visited = []):
    visited.append(start)

    for computer in graph[start]:
        if computer not in visited:
            dfs(connect, computer, visited)

    return visited

print(len(dfs(connect, 1, visitedList)) - 1)
