#baekjoon - 1018 - 체스판 다시 칠하기
import sys


class Main:
    y, x = int(sys.stdin.readline().split(' '))
    chess = []
    count = 0
    paint_count = 0

    for _ in range(y):
        chess.append(sys.stdin.readline())

    for i in range(y):
        for j in range(x-8+1):
            for z in range(j, j+8):
                if z == 0 :
                    continue
                else:
                    if chess[i][z] == chess[i][z-1]:
                        count += 1