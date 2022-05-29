#9461 파도반 수열
import sys

n = int(sys.stdin.readline())
result = []
p = {1:1, 2:1, 3:1, 4:2, 5:2}

# P(n) = P(n-1)+ P(n-5)
for _ in range(n):
    a = int(sys.stdin.readline())
    if p.get(a):
        result.append(p.get(a))
    else:
        for i in range(6, a+1):
            if p.get(i):
                continue
            else:
                p[i] = p.get(i-1)+p.get(i-5)
        result.append(p.get(a))

for _ in result:
    print(_)
