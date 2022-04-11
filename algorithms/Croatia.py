#baekjoon - 2941 - 크로아티아 알파벳

class Main:
    str = list(input())
    count = 0

    for i in range(len(str)):
        if str[i] == '':
            continue
        elif str[i] == 'c' and (str[i+1] == '=' or str[i+1] == '-') :
            str[i]=''
            str[i+1]=''
            count += 1
        elif str[i] == 'd':
            if str[i+1] == 'z' and str[i+2] == '=':
                str[i]=''
                str[i+1]=''
                str[i+2]=''
                count += 1
            elif str[i+1] == '-':
                str[i]=''
                str[i+1]=''
                count += 1
        elif (str[i] == 'l' or str[i] == 'n') and str[i+1] == 'j':
            str[i]=''
            str[i+1]=''
            count += 1
        elif (str[i] == 's' or str[i] == 'z') and str[i+1] == '=':
            str[i]=''
            str[i+1]=''
            count += 1

    for i in str:
        if i != '':
            count += 1

    print(count)

