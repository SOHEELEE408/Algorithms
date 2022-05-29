#baekjoon - 11651 - 좌표 정렬하기2

a = int(input())

coos = []

for _ in range(a):
    x, y = map(int, input().split())
    coos.append([y, x])

coos.sort()

for _ in range(a):
print(coos[_][1], coos[_][0])