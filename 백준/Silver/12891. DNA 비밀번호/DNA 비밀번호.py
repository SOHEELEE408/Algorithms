import sys

input = sys.stdin.readline

s, p = map(int, input().split())
i = 0
j = p-1
dna = list(input())
A, C, G, T = map(int, input().split())
dic = { 'A': 0, 'C': 0, 'G': 0, 'T': 0}
temp = dna[i:j]

for _ in temp:
    dic[_] += 1
cnt = 0

while j < s:
    dic[dna[j]] += 1
    if(dic['A'] >= A and dic['C'] >= C and
        dic['G'] >= G and dic['T'] >= T):
            cnt += 1
    dic[dna[i]] -= 1
    i += 1
    j += 1

print(cnt)