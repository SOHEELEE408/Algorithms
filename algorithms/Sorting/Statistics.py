#baekjoon - 2108 - 통계학
import sys

a = int(sys.stdin.readline())
nums = {}
nums2 = []
total = 0

for _ in range(a):
    number = int(sys.stdin.readline())
    total += number
    if _ == 0:
        nums[number] = 1
    else:
        if number in nums:
            nums[number] += 1
        else:
            nums[number] = 1

# 평균
print(round(total/a))

# 중앙값
sorted_nums = sorted(nums.keys())
print(sorted_nums)

for i in range(len(sorted_nums)):
    for j in range(sorted_nums[i][1]):
        nums2.append(sorted_nums[i][0])

print(nums2[a//2])

sorted_nums = sorted(nums.items())
mid = a//2
for i in range(len(sorted_nums)):
    mid -= sorted_nums[i][1]
    if mid < 0:
        print(sorted_nums[i][0])
        break

# 최빈값
print(max(nums, key = nums.get))

# 범위
print(max(nums)-min(nums))