#baekjoon - 10809 - 알파벳 찾기

class Main:
    word = input()

    for i in range(26):
        a = chr(i+97)
        b = -1
        for j in range(len(word)):
            if a==word[j:j+1]:
                b=j
                break
        print(b,end=' ')