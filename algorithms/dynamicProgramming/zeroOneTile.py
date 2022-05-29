#1904 01타일

import sys

n = int(sys.stdin.readline())
result = [0,1,2]

def dp(n):
    if n == 1:
        return result[1]
    elif n == 2:
        return result[2]
    else:
        return dp(n-1)+dp(n-2) #리턴값이 너무 클 경우 "런타임에러"날 수 있음


print(dp(n)%15746)





















"""
zeroc = n//2
count = 0

for i in range(zeroc+1):
    if i == 0:
        count += 1
    else:
        onec = n-2*i
        temp1 = 1
        temp2 = 1
        for j in range(onec):
            temp1 *= (i+onec-j)
            temp2 *= (j+1)

        count += (temp1//temp2)

print(count%15746)

result = {0:0,1:1,2:2}

def dp(n):
    if n == 1:
        return result.get(1)
    elif n == 2:
        return result.get(2)
    else:
        if result.get(n):
            return result[n]
        else:
            result[n] = result.get(n-2)+result.get(n-1)
        return result.get(n)


print(dp(n)%15746)

import sys

n = int(sys.stdin.readline())
n1 = 1
n2 = 2
res = 0


if n == 1:
    res = n1
elif n == 2:
    res = n2
else:
    for _ in range(3, n+1):
        res = (n1+n2)%15746
        n1, n2 = n2, res #메모리를 적게

print(res)

#순열 조합 라이브러리
#동적계획법 문제는 동적계획법으로만 풀어야 한다.
"""