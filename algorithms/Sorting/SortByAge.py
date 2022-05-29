#baekjoon - 10814 - 나이순 정렬

a = int(input())
member = []

for _ in range(a):
    age, name = input().split()
    member.append([int(age), name])

member.sort(key=lambda x:x[0])

for i in member:
    print(i[0],i[1])


# 딕셔너리
# join
# sorted 아스키코드로 문자열 숫자 정열
# map
# count
# 자료구조