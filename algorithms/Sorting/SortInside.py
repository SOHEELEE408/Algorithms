#baekjoon - 1427 - 소트인사이드

num_str = list(input())

num_int = sorted(list(map(int, num_str)), reverse=True)

for _ in range(len(num_int)):
    print(num_int[_], end='')


