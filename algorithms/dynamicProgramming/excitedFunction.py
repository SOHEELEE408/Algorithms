#9184 신나는 함수 실행
import sys
"""
results = []
ws = {}


def w(a, b, c):
    if ws.get('w('+str(a)+', '+str(b)+', '+str(c)+')') == None:
        ws['w('+str(a)+', '+str(b)+', '+str(c)+')'] = 0
    else:
        return ws['w('+str(a)+', '+str(b)+', '+str(c)+')']


    if a<=0 or b<=0 or c<=0:
        ws['w('+str(a)+', '+str(b)+', '+str(c)+')'] = 1
        return 1

    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)

    elif a<b and b<c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        return w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)


def dp():
    a, b, c = map(int, sys.stdin.readline().split())
    while a != -1 and b != -1 and c != -1:
        result = w(a, b, c)
        results.append('w('+str(a)+', '+str(b)+', '+str(c)+') = '+str(result))
        a, b, c = map(int, sys.stdin.readline().split())

    for _ in results:
        print(_)


dp()
"""

results = []

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1

    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)

    if dp[a][b][c]:
         return dp[a][b][c]

    elif a<b and b<c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        dp[a][b][c] = w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)

    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        for _ in results:
            print(_)
        break
    result = w(a, b, c)
    results.append('w('+str(a)+', '+str(b)+', '+str(c)+') = '+str(result))

