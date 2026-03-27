# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
# 동전 종류 수 N, 목표 금액 K 입력받기
N, K = map(int, input().split())

# 동전 가치를 저장할 리스트
coins = []

# N개의 동전 가치를 입력받아서 리스트에 추가
for _ in range(N):
    coins.append(int(input()))

# 사용한 동전 개수를 저장할 변수
count = 0

# 큰 동전부터 써야 하므로 뒤에서부터 확인
for i in range(N - 1, -1, -1):
    # 현재 동전을 몇 개 사용할 수 있는지 계산
    count += K // coins[i]

    # 그 동전들을 사용하고 남은 금액으로 갱신
    K %= coins[i]

# 최소 동전 개수 출력
print(count)