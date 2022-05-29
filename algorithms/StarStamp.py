#baekjoon - 2447 - 별 찍기10
import math


class Main:
    n = int(input())
    empty_x = []
    empty_y = []

    for i in range(int(math.log(n,3))):
        for j in range(int(n/int(pow(3,(i+1)))), int(n/int(pow(3,(i+1)))*2)):
            empty_x.append(j)
            empty_y.append(j)

    print(empty_x)

    for y in range(n):
        for a in range(3):
            if a != 1:
                for x in range(n):
                    if x in empty_x:
                        print(' ',end='')
                    else:
                        print('*',end='')
                    if x == n-1:
                        print('')
            else :
                for x in range(n):




