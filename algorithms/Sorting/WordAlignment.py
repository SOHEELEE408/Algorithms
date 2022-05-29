#baekjoon - 1181 - 단어 정렬하기
import sys

a = int(sys.stdin.readline().strip())
words2 = set()

for _ in range(a):
    words2.add(sys.stdin.readline().strip())

words2 = sorted(words2)
words = list(words2)
words.sort(key=len)

for _ in words:
    print(_)