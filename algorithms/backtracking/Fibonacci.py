#baekjoon - 1003 - 피보나치 함수
import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

for _ in range(len(nums)):
    zero_one = [1, 0]
    for i in range(nums[_]):
        temp_zero = zero_one[1]
        temp_one = zero_one[0]+zero_one[1]
        zero_one[0] = temp_zero
        zero_one[1] = temp_one
    print('{} {}'.format(zero_one[0], zero_one[1]))
"""
    
점화식

f(n)이 반환할 값을 생각한다. 

우선 순위 큐 heapque, prioty que

이진 탐색 : 바이섹? logN

백트래킹 

힙의 종류 공부

정확성과 효율성 따로 점수 매긴다 >> 관련 자료구조, 함수를 사용해야 함

"""