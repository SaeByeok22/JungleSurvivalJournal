# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

# n 입력받기
n = int(input())

# ===== base case =====
# n이 0이면 바로 0 출력
if n == 0:
    print(0)

# n이 1이면 바로 1 출력
elif n == 1:
    print(1)
# =====================
# 그 외에는 반복문으로 피보나치 계산
else:
    a, b = 0, 1  # a = F(0), b = F(1)

    # 2부터 n까지 차례대로 계산
    for _ in range(2, n + 1):
        a, b = b, a + b

    # b에 F(n)이 저장되어 있음
    print(b)