import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    ms = list(input())
    for j in range(M):
        maze[i][j] = int(ms[j])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(n, m):

    queue = deque()
    queue.append((n, m))
    visited[n][m] = True

    while queue:
        node = queue.popleft()
        for _ in range(4):
            x = node[0] + dx[_]
            y = node[1] + dy[_]
            if x >= 0 and y >= 0 and x < N and y < M:
                if maze[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    maze[x][y] = maze[node[0]][node[1]] + 1
                    queue.append((x, y))


bfs(0, 0)

print(maze[N-1][M-1])

