import sys

input = sys.stdin.readline

n = int(input())
nums = [0]*n
stack = []
result = ""
success = True
top = 1

for _ in range(n) :
    nums[_] = int(input())

for _ in nums :
    if _ >= top:
        while _ >= top :
            stack.append(top)
            top += 1
            result += '+\n'
        stack.pop()
        result += '-\n'
    else:
        i = stack.pop()
        if i > _:
            print('NO')
            success = False
            break
        else:
            result += '-\n'

if success:
    print(result)
