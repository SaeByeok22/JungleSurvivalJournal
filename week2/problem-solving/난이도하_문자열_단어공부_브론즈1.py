# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 문제 푸는 방법..?
# 인풋 받기..
import sys
input = sys.stdin.readline

# 다 대문자로 만들어서 편하게 만들기
word = input().rstrip().upper()
count = [0] * 26

# 알파벳을 보면서 카운팅하기.
for w in word:
    count[ord(w) - ord('A')] += 1

max_count = max(count)

# 최대 횟수인 알파벳이 2개 이상이면 ? 출력하고, 아니면 해당 알파벳 출력
if count.count(max_count) > 1:
    print('?')
else:
    print(chr(count.index(max_count) + ord('A')))