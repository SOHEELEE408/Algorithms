# 부분집합 구하기

arry = list(input().split())

def BT(index, result):
    if index == len(arry):
        print(result)
        return

    result.append(arry[index])
    BT(index+1, result)
    result.pop()
    BT(index+1, result)

BT(0, [])