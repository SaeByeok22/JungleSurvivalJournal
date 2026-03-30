# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

n, m = len(A), len(B)

dp = [0] * (m + 1)

for i in range(1, n + 1):
    prev = 0  # dp[i-1][j-1]
    for j in range(1, m + 1):
        temp = dp[j]  # dp[i-1][j] 저장

        if A[i - 1] == B[j - 1]:
            dp[j] = prev + 1
        else:
            dp[j] = max(dp[j], dp[j - 1])

        prev = temp

print(dp[m])