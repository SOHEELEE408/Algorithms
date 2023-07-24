import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
result = 0

def merge_sort(unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList

    mid = len(unsortedList)//2 # 리스트 반으로 쪼개기
    left = unsortedList[:mid]
    right = unsortedList[mid:]

    # 쪼갠 리스트 각각 merge sort 진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_, right_)

def merge(left, right):
    global result
    i, j, k = 0, 0, 0
    sortedList = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            result = result + (len(left)-i)
            sortedList.append(right[j])
            j += 1
    while i < len(left): # 왼쪽 부분 집합만 데이터 남은 경우
        sortedList.append(left[i])
        i += 1
    while j < len(right): # 오른쪽 부분 집합만 데이터 남은 경우
        sortedList.append(right[j])
        j += 1
    return sortedList

merge_sort(numbers)
print(result)