import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque()

for _ in range(1, n+1):
    cards.append(_)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())
