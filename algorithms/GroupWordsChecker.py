#baekjoon - 1316 - 그룹 단어 체커

class Main:
    number = int(input())
    count = 0

    for i in range(number):
        same = 1
        word = input()

        for j in range(len(word)):
            print('처음 j : ', j)
            if (j == 0 and word.count(word[j]) != 1) or (word.count(word[j]) != 1 and word[j] != word[j-1]):
                print('같은 알파벳 있음 :', word[j])
                for k in range(j, j+word.count(word[j])):
                    if k > len(word)-1:
                        break
                    print('j : ', j, 'k : ', k)
                    if word[j] != word[k]:
                        print('same 0 됨')
                        same = 0

            if same == 0:
                break;

        if same == 1:
            print('단어 인정 :', word)
            count += 1

    print(count)