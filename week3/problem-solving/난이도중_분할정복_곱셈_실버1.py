# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 1:
        return a % c

    half = power(a, b // 2, c)

    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

print(power(A, B, C))