#baekjoon - 5622 - 다이얼

class Main:
    str = input()
    alphabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    time = 0

    for i in range(len(str)):
        for j in range(len(alphabets)):
            if alphabets[j].find(str[i]) == -1:
                continue
            else:
                time+=j+3

    print(time)

