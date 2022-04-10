#baekjoon - 1157 - 단어공부

class Main:
    str = input().upper()
    str_list = list(set(str))
    cnt = []

    for i in str_list:
        cnt.append(str.count(i))

    if cnt.count(max(cnt)) > 1:
        print("?")
    else:
        print(str_list[cnt.index(max(cnt))])