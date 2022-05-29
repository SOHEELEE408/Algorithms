#baekjoon - 14888 - 연산자 끼워넣기
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sum, minus, multi, div = map(int, sys.stdin.readline().split())
MIN = 1e9
MAX = -1e9

def BT(x, temp):
    global sum, minus, multi, div, MIN, MAX
    if sum == 0 and minus == 0 and multi == 0 and div == 0:
        MIN = min(MIN, temp)
        MAX = max(MAX, temp)
        return
    else:
        if sum > 0:
            sum -= 1
            BT(x+1, temp + nums[x])
            sum += 1
        if minus > 0:
            minus -= 1
            BT(x+1, temp - nums[x])
            minus += 1
        if multi > 0:
            multi -= 1
            BT(x+1, temp * nums[x])
            multi += 1
        if div > 0:
            div -= 1
            BT(x+1, int(temp/nums[x]))
            div += 1

BT(1, nums[0])

print(MAX)
print(MIN)