#baekjoon - 10989 - 수 정렬하기3
import sys

class Main:
    number = int(sys.stdin.readline())
    nums = [0] * 10001

    for i in range(number):
        input_num = int(sys.stdin.readline())
        nums[input_num] += 1

    for i in range(10001):
        if nums[i] != 0:
            for _ in range(nums[i]):
                print(i)

# if __name__ == '__main__' :

"""
    sorted ,sort 
    안정정렬 - 같은 값일 경우는 순서가 바뀌지 않도록 하기, 파이썬은 알아서 해줌
    round() 반올림 함수 사사오익 짝수로 맞춰줘야 한다. 
"""
