# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

# 슈도 코드...
# input N
# input W[N][N]

# answer = INF
# visited = [False] * N

# function dfs(start, now, count, cost):
#     if cost >= answer:
#         return

#     if count == N:
#         if W[now][start] != 0:
#             total_cost = cost + W[now][start]
#             answer = min(answer, total_cost)
#         return

#     for next in 0..N-1:
#         if visited[next]:
#             continue
#         if W[now][next] == 0:
#             continue

#         visited[next] = True
#         dfs(start, next, count + 1, cost + W[now][next])
#         visited[next] = False

# visited[0] = True # 출발도시도 방문햇다고 생각함.
# dfs(0, 0, 1, 0)

# print(answer)

import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
answer = INF
visited = [False] * N

def dfs(start, now, count, cost):
    global answer

    if cost >= answer:
        return

    if count == N:
        if W[now][start] != 0:
            answer = min(answer, cost + W[now][start])
        return

    for next in range(N):
        if visited[next]:
            continue
        if W[now][next] == 0:
            continue

        visited[next] = True
        dfs(start, next, count + 1, cost + W[now][next])
        visited[next] = False

visited[0] = True
dfs(0, 0, 1, 0)

print(answer)