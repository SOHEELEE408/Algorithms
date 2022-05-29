#baekjoon - 7568 - 덩치
import sys


class Main:
    n = int(sys.stdin.readline())
    people = []

    for _ in range(n):
        values = input().split(' ')
        people.append(values)