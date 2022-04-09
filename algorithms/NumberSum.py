#baekjoon - 11720 - 숫자의 합

class Main:
    a = input();
    b = input();
    hap = 0;

    for i in range(int(a)):
        hap=hap+int(b[i:i+1])

    print(hap);