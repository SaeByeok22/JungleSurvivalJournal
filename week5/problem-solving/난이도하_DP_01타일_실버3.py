# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
# 만들려는 타일 길이 n을 입력받음
n = int(input())

# a는 dp[1] = 1, b는 dp[2] = 2를 의미
a, b = 1, 2

# n=1이면 반복 안 하고 바로 a 출력
# n=2 이상이면 n-1번 갱신해서 답까지 감
for _ in range(n - 1):
    # 다음 피보나치 형태 값으로 갱신
    # 새 a = 이전 b
    # 새 b = 이전 a + 이전 b (단, 15746으로 나눈 나머지)
    a, b = b, (a + b) % 15746

# 최종적으로 a에 dp[n]이 들어 있으므로 출력
print(a)