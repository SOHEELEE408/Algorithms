import sys

input = sys.stdin.readline
N = int(input())

prime = [2, 3, 5, 7]
result = []

def isPrime(num):
    for _ in range(2, num//2+1):
        if num%_ == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == N:
        result.append(num)
        return

    for n in range(1, 10):
        newNum = int(str(num)+str(n))
        if isPrime(newNum):
            dfs(newNum)

for _ in prime:
    dfs(_)

result.sort()
for _ in result:
    print(_)