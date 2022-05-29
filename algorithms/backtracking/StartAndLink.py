#baekjoon - 14889 - 스타트와 링크
import sys

n = int(sys.stdin.readline())
team = [0 for _ in range(n)]
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dif_min = 1e9

def BT(x, y):
    global dif_min
    if x == int(n/2):
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if team[i] == 1 and team[j] == 1:
                    start += s[i][j]
                elif team[i] == 0 and team[j] == 0:
                    link += s[i][j]
        dif_min = min(dif_min, abs(start-link))
        return
    for i in range(y, n):
        if team[i] == 0:
            team[i] = 1
            BT(x+1, i+1)
            team[i] = 0

BT(0, 0)
print(dif_min)