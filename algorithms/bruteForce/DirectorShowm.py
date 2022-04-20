#baekjoon - 1436 - 영화감독 숌
import sys

class Main:
    serise = int(sys.stdin.readline())
    title = 666

    while serise != 1:
        title += 1
        if str(title).count('666') > 0:
            print(title)
            serise -= 1

    print(title)
