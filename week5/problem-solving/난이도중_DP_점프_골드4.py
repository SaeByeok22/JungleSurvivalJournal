# DP - 점프 (백준 골드4)
# 문import sys
import sys
input = sys.stdin.readline

# n: 마지막 돌 번호, m: 못 밟는 돌 개수
n, m = map(int, input().split())

# 못 밟는 돌 리스트
n_list = []
for _ in range(m):
    a = int(input())
    n_list.append(a)

# 최대 속도 설정 (이 이상은 의미 없음)
# 점점 속도가 커지더라도 sqrt(2n) 정도면 충분
max_speed = int((2 * n) ** 0.5) + 1

# dp 배열 만들기
# dp[i][j] = i번 돌에 속도 j로 도착했을 때 최소 점프 횟수
dp = [[float('inf')] * (max_speed+1) for _ in range(n+1)]

# 시작 상태: 1번 돌에서 속도 0으로 시작 (점프 0번)
dp[1][0] = 0


def fun():
    # 1번 돌부터 n번 돌까지 하나씩 계산
    for i in range(1, n+1):
        stone = i

        # 못 밟는 돌이면 그냥 넘어감
        if stone in n_list:
            continue

        # 가능한 속도들
        for j in range(1, max_speed):
            v = j

            # 이전 위치 = 현재 위치 - 속도
            # 거기에서 v-1, v, v+1 속도로 왔을 수 있음
            dp[stone][v] = min(
                dp[stone - v][v-1],  # 속도 줄이고 점프
                dp[stone - v][v],    # 같은 속도로 점프
                dp[stone - v][v+1]   # 속도 늘리고 점프
            ) + 1  # 이번 점프 1번 추가

    return dp

# DP 실행
result = fun()

# n번 돌에 도착하는 최소 점프 횟수
min_jumps = min(dp[n])

# 도달 못하면 -1
if min_jumps == float('inf'):
    print(-1)
else:
    print(min_jumps)