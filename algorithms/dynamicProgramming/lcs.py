import sys
from itertools import combinations

str1 = list(input())
str2 = list(input())

count = 0
str_len = 0

if len(str1) > len(str2):
    str_len = len(str1)
else:
    str_len = len(str2)

for i in range(str_len, 2, -1):
    result1 = list(combinations(str1, i))
    result2 = list(combinations(str2, i))
    for res in result2:
        if res in result1:
            count = len(res)
            break
    if count != 0:
        break

print(count)
