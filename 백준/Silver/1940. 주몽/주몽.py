import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
materials = list(map(int, input().split()))
cnt = 0


for _ in materials:
    temp = m - _
    if(materials.count(temp) == 1 and _ != temp):
        cnt += 1
        materials.remove(temp)


print(cnt)