import sys

class Main:
    number = int(sys.stdin.readline())
    nums = []

    for _ in range(number):
        nums.append(int(sys.stdin.readline()))

    nums.sort()

    for _ in range(number):
        print(nums[_])