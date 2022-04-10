#baekjoon - 117214 - 문자열 반복

class Main:
    t = int(input())

    for i in range(t):
        r,s = input().split()
        for j in range(len(s)):
            print(s[j]*int(r),end='')
        print()