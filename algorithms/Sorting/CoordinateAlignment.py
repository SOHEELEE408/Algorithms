#baekjoon - 11650 - 좌표 정렬하기

a = int(input())

coos = []

for _ in range(a):
    coos.append(list(map(int, input().split())))

coos.sort()

for _ in range(a):
    print(coos[_][0], coos[_][1])