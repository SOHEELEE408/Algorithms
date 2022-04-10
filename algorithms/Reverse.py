#baekjoon - 2908 - 상수

class Main :
    nums = input().split()

    num1 = int("".join(reversed(nums[0])))
    num2 = int("".join(reversed(nums[1])))
    if num1 > num2 :
        print(num1)
    else:
        print(num2)