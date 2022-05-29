#baekjoon - 10870 - 피보나치 수5

class Main:
    number = int(input())
    total = []

    for i in range(number+1):
        if i < 2:
            total.append(i)
        else :
            temp = total[len(total)-2] + total[len(total)-1]
            total.append(temp)

    print(total[len(total)-1])

