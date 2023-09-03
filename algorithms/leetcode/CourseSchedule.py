import sys

sys.setrecursionlimit(10**6)

numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
visited = [False] * numCourses
finished = [False] * numCourses
graph = [[] for _ in range(numCourses)]
cycle = 0
dfsCount = 0

for prerequisite in prerequisites:
    graph[prerequisite[0]].append(prerequisite[1])


def dfs(course):
    global cycle, dfsCount

    dfsCount += 1

    visited[course] = True
    for pre in graph[course]:
        if not visited[pre]:
            dfs(pre)
        elif not finished[pre]:
            cycle = cycle + 1

    finished[course] = True


for _ in range(numCourses):
    if not visited[_]:
        dfs(_)

if cycle == 0:
    print(True)
else:
    print(False)