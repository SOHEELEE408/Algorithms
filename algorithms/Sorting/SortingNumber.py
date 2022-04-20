#baekjoon - 2750 - 수 정렬하기

class Main:
    number = int(input())
    nums = []

    for _ in range(number):
        nums.append(int(input()))

    nums.sort()

    for _ in range(number):
        print(nums[_])
