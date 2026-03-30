# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    # m원을 만드는 방법 수
    dp = [0] * (M + 1)

    # 0원을 만드는 방법은 1개
    dp[0] = 1

    # 동전을 하나씩 사용하면서 경우의 수 누적
    for coin in coins:
        for money in range(coin, M + 1):
            dp[money] += dp[money - coin]

    print(dp[M])