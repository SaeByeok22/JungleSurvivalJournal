# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 동전 종류 개수
    N = int(input())

    # 사용할 수 있는 동전들
    coins = list(map(int, input().split()))

    # 만들어야 하는 목표 금액
    M = int(input())

    # dp[x] = x원을 만드는 방법의 수
    # 인덱스가 곧 "현재 금액"을 의미함
    dp = [0] * (M + 1)

    # 0원을 만드는 방법은 "아무 동전도 선택하지 않는 경우" 1가지
    # 이 값이 있어야 이후 dp[coin], dp[coin + ...] 들이 누적될 수 있음
    dp[0] = 1

    # 동전을 하나씩 확인하면서 경우의 수를 누적
    # 바깥쪽 반복문을 동전으로 두는 이유:
    # 같은 조합을 순서만 바꿔서 중복 계산하지 않기 위해서
    # 예) 1+2 와 2+1 을 같은 경우로 처리
    for coin in coins:

        # 현재 동전 coin을 사용해서 만들 수 있는 금액들을 갱신
        # coin보다 작은 금액은 이 동전을 한 번도 사용할 수 없으므로 시작점을 coin으로 잡음
        for money in range(coin, M + 1):

            # money원을 만드는 경우의 수에
            # (money - coin)원을 만든 뒤 현재 동전 coin을 하나 추가하는 경우를 더함
            #
            # 예를 들어 coin=2, money=5 라면:
            # 5원을 만드는 방법 += 3원을 만드는 방법 수
            # 즉, "3원을 만드는 모든 경우" 뒤에 2원을 하나 붙이면 5원이 됨
            dp[money] += dp[money - coin]

    # 목표 금액 M원을 만드는 총 경우의 수 출력
    print(dp[M])