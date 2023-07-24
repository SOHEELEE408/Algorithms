import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
maxScore = max(scores)
total = 0

for _ in scores:
    total += _

average = (total/maxScore*100)/n

print(average)