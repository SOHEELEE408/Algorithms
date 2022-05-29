#baekjoon - 2580 - 스도쿠
import sys

s = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
done = False

def BT(a,b):
    global done
    if a == 8:
        for row in s:
            if 0 in row:
                done = False
                break
            elif 0 not in row:
                done = True
        if done:
            for _ in range(9):
                print(" ".join(str(i) for i in s[_]))
            return
    for i in range(a, 9):
        for j in range(b, 9):
            if s[i][j] != 0:
                continue
            else:
                can = [1,2,3,4,5,6,7,8,9]
                for r in range(9):
                    if s[r][j] in can:
                        can.remove(s[r][j])
                for c in range(9):
                    if s[i][c] in can:
                        can.remove(s[i][c])
                for r in range(i-(i%3), i-(i%3)+3):
                    for c in range(j-(j%3), j-(j%3)+3):
                        if s[r][c] in can:
                            can.remove(s[r][c])
                for n in can:
                    s[i][j] = n
                    BT(i, 0)

BT(0,0)