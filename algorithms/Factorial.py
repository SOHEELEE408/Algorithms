#baekjoon - 10872 - 팩토리얼

class Main:
    number = int(input())
    total = 1

    if number == 0 :
        print(total)
    else:
        for i in range(number):
            total *= (i+1)
        print(total)