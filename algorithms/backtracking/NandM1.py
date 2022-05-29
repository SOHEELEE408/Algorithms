#baekjoon - 15649 ~ 15652 - N과 M
import copy

n, m = list(map(int, input().split()))
nums = []

def dfs1(x):
    #global nums
    if x == m:
        print(" ".join(str(i) for i in nums))
        return
    for i in range(1, n+1):
        if i not in nums:
            nums.append(i)
            dfs1(x+1)
            nums.pop()

dfs1(0)

###############################

def dfs2(x):
    if x == m:
        print(" ".join(str(i) for i in nums))
        return
    for i in range(1, n+1):
        if i not in nums:
            if x == 0 or nums[len(nums)-1]<i:
                nums.append(i)
                dfs2(x+1)
                nums.pop()

dfs2(0)

################################

def dfs3(x):
    if x == m:
        print(" ".join(str(i) for i in nums))
        return
    for i in range(1, n+1):
        nums.append(i)
        dfs3(x+1)
        nums.pop()

############################################

def dfs4(x):
    if x == m:
        print(" ".join(str(i) for i in nums))
        return
    for i in range(1, n+1):
        if x == 0 or nums[len(nums)-1] <= i:
            nums.append(i)
            dfs4(x+1)
            nums.pop()

dfs4(0)


# 얕은 복사 - 주소만 복사 - sort / 깊은 복사 - sorted b = a[:]
# copy.deepcopy()