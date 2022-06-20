#12865 평범한 배낭
import sys

max_num, max_w = map(int, sys.stdin.readline().split())
things = [[0,0]]
bag = [[0 for i in range(max_w+1)] for j in range(max_num+1)]

for _ in range(max_num):
    things.append(list(map(int, sys.stdin.readline().split())))


for i in range(1, max_num+1):
    for j in range(1, max_w+1):
        weight = things[i][0]
        value = things[i][1]

        if j < weight:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(value+bag[i-1][j-weight], bag[i-1][j])

print(bag[max_num][max_w])


#bag[i][j] = max(현재 물건 가치 + bag[이전 물건][현재 가방 무게 - 현재 물건 무게], bag[이전 물건][현재 가방 무게])
#bisect