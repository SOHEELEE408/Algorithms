#baekjoon - 9663 - N-Queen
import sys

n = int(sys.stdin.readline())
count = 0
isused1 = [0 for _ in range(n)] # 세로
isused2 = [0 for _ in range(2*n-1)] # 위>아 대각선
isused3 = [0 for _ in range(2*n-1)] # 아>위 대각선

def BT(cur):
    global count
    if cur == n:
        count += 1
        return

    for i in range(n):
        if isused1[i] == 1 or isused2[i+cur] == 1 or isused3[cur-i+n-1] == 1:
            continue
        isused1[i] = 1
        isused2[i+cur] = 1
        isused3[cur-i+n-1] = 1

        BT(cur+1)
        isused1[i] = 0
        isused2[i+cur] = 0
        isused3[cur-i+n-1] = 0


BT(0)
print(count)

"""
def BT(index, x, pos):
    global count
    temp = "".join(str(i) for i in pos)
    if len(pos) == n and temp not in result:
        result.append(temp)
        print(result)
        count += 1
        return

    for y in range(n):
        if y != pos[len(pos)-1]-1 and y != pos[len(pos)-1] and y != pos[len(pos)-1]+1 and y not in pos:
            pos.append(y)
            BT(index, x+1, pos)
    if pos[0] != n-1:
        BT(index+1, 0, [index+1])


BT(0, 0, [0])


def BT(x, y, index):
    global count
    if x == n-1:
        count += 1
        return

    isused1[y] = 1
    isused2[x-y+n-1] = 1
    isused3[x+y] = 1

    for i in range(n):
        if isused1[i] == 0 and isused2[x+1-i+n-1] == 0 and isused3[x+1+i] == 0:
            BT(x+1, i, index)

    for _ in range(2*n-1):
        isused2[_]=0
        isused3[_]=0

    for _ in range(n):
        isused1[_]=0

    if index == n-1:
        return
    else:
        isused1[index+1+1] = 1
        isused2[0-index+1+1+n-1] = 1
        isused3[index+1+1] = 1
        BT(0, index+1, index+1)

"""
