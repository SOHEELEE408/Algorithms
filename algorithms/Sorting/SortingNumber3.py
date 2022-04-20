#baekjoon - 10989 - 수 정렬하기3
import sys

class Main:
    number = int(sys.stdin.readline())
    nums = [0] * 10001

    for i in range(number):
        input_num = int(sys.stdin.readline())
        nums[input_num] += 1

    for i in range(10001):
        if nums[i] != 0:
            for _ in range(nums[i]):
                print(i)