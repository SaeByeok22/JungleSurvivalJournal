# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

two_sum = set()

# x + y 전부 저장 (같은 수 두 번 사용 가능)
for i in range(n):
    for j in range(i, n):
        two_sum.add(arr[i] + arr[j])

# 가장 큰 수부터 확인
for i in range(n - 1, -1, -1):
    k = arr[i]
    for j in range(i + 1):
        if k - arr[j] in two_sum:
            print(k)
            sys.exit()