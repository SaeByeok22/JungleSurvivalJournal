# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

import sys

input = sys.stdin.readline

word = input().rstrip().upper()
count = [0] * 26

for w in word:
    count[ord(w) - ord('A')] += 1

max_count = max(count)

if count.count(max_count) > 1:
    print('?')
else:
    print(chr(count.index(max_count) + ord('A')))