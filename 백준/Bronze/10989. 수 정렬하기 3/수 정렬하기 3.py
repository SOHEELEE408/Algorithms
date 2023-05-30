import sys

input = sys.stdin.readline
n = int(input())
numbers = [0] * 10001

for _ in range(n):
    numbers[int(input())] += 1

for _ in range(10001):
    if numbers[_] != 0:
        for cnt in range(numbers[_]):
            print(_)