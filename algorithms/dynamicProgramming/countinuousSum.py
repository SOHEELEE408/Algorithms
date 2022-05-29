import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sum2 = [nums[0]]

for i in range(len(nums)-1):
    sum2.append(max(sum2[i]+nums[i+1], nums[i+1])) #제일 마지막 값을 포함한 연속합

print(max(sum2))

#연속합(누적합) 문제들