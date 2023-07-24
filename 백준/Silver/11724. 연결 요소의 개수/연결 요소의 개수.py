import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = []
result = 0

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs_recursive(graph, start, visited = []):
    global result

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)

    return visited

for _ in range(1, n+1):
    if _ not in visited:
        result += 1
        dfs_recursive(graph, _, visited)
print(result)