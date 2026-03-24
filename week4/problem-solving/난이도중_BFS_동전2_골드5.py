# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

dp = [100001] * (k + 1)
dp[0] = 0

for coin in arr:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(-1 if dp[k] == 100001 else dp[k])