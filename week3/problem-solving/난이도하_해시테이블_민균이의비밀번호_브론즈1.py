# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

n = int(input())
words = set()

for _ in range(n):
    w = input().strip()
    words.add(w)

for w in words:
    if w[::-1] in words:
        length = len(w)
        mid = w[length // 2]
        print(length, mid)
        break