# 문자열 - 광고 (백준 플래4)
# 문제 링크: https://www.acmicpc.net/problem/1305
l = int(input())
s = input().strip()

pi = [0] * l
j = 0

for i in range(1, l):
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j += 1
        pi[i] = j

print(l - pi[-1])