# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline

# 두 문자열 입력
A = input().strip()
B = input().strip()

# 문자열 길이
n, m = len(A), len(B)

# dp[j] = 현재까지 A의 i번째 문자까지 고려했을 때,
#         B의 j번째 문자까지의 LCS 길이
# (2차원 dp[i][j]를 1차원으로 압축한 형태)
dp = [0] * (m + 1)

# A를 앞에서부터 하나씩 늘려가며 계산
for i in range(1, n + 1):

    # prev = dp[i-1][j-1] 역할 (왼쪽 위 값)
    # 처음 j=1일 때는 dp[i-1][0]이라서 0으로 시작
    prev = 0  

    # B도 앞에서부터 하나씩 비교
    for j in range(1, m + 1):

        # temp = dp[i-1][j] (현재 dp[j]는 아직 이전 행 값)
        temp = dp[j]

        # 현재 문자 비교
        if A[i - 1] == B[j - 1]:
            # 문자가 같으면 LCS 길이 +1
            # (왼쪽 위 값 + 1)
            dp[j] = prev + 1
        else:
            # 다르면
            # 위(dp[i-1][j]) vs 왼쪽(dp[i][j-1]) 중 큰 값
            dp[j] = max(dp[j], dp[j - 1])

        # 다음 j를 위해 prev를 갱신
        # (이제 prev는 dp[i-1][j]가 됨)
        prev = temp

# 최종 결과: A 전체와 B 전체의 LCS 길이
print(dp[m])