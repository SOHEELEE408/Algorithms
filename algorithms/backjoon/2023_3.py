# 신기한 소수 찾기 - 세 번째 복습
# 핵심: 소수 임을 확인하기 위한 나눗셈 연산을 어느 범위까지 수행할 것인가 ➡ 2~자신의 절반

import sys

input = sys.stdin.readline

N = int(input())
result = []

def isPrime(number):

    for n in range(2, number//2):
        if number % n == 0:
            return False

    return True


def dfs(number):
    if len(str(number)) == N and isPrime(number):
        result.append(number)
        return

    if(isPrime(number)):
        for _ in range(1, 10):
            dfs(int(str(number)+str(_)))

primes = [2, 3, 5, 7]

for prime in primes:
    dfs(prime)

result.sort()

for _ in result:
    print(_)

