import sys

input = sys.stdin.readline
nums = []
result = []

for _ in range(5):
    a = list(map(str, input().split()))
    nums.append(a)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    for k in range(4):
        ddx = x+dx[k]
        ddy = y+dy[k]

        if 0 <= ddx < 5 and 0<=ddy<5:
            dfs(ddx, ddy, number+nums[ddx][ddy])

for i in range(5):
    for j in range(5):
        dfs(i, j, nums[i][j])

print(len(result))