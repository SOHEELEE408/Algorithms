import sys

input = sys.stdin.readline
n = int(input())

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for _ in range(n):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(a*b//g)