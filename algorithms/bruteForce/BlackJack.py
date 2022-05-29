#baekjoon - 2798 - 블랙잭

class Main:
    n, m = input().split(' ')
    cards = input().split(' ')
    sums = []
    sum = 0

    for i in range(len(cards)-1):
        sums.append(int(cards[i])+int(cards[i+1]))

    print(sums)

    for i in range(len(sums)):
        for j in range(len(cards)):
            if j != i and j != (i+1) and sums[i] < int(m):
                print('sums[',i, '] :', sums[i], 'card[',j,'] : ', cards[j])
                print('sum :', sums[i]+int(cards[j]))
                if sums[i]+int(cards[j]) == int(m) or (sum < sums[i]+int(cards[j]) and sums[i]+int(cards[j]) < int(m)):
                    sum = sums[i]+int(cards[j])
                    break
        if sum == int(m):
            break
    print(sum)

"""
    for i in range(len(sums)):
        #if sums[i] < int(m):
            for j in range(len(cards)-2):
                if sums[i]+int(cards[j+2]) == int(m):
                    sum = sums[i]+int(cards[j+2])
                    print('card[',j+2,'] : ', cards[j+2],'sum :', sum)
                    break
                elif sums[i]+int(cards[j+2]) < int(m) and sums[i]+int(cards[j+2]) > sum:
                    sum = sums[i]+int(cards[j+2])
                    print('card[',j+2,'] : ', cards[j+2],'sum :', sum)
            if sum == int(m):
                break
"""
