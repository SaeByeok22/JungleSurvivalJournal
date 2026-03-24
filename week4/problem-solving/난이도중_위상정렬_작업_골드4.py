# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    cnt = data[1]
    for pre in data[2:2 + cnt]:
        graph[pre].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(max(dp))