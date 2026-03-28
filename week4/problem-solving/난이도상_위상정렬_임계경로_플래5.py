# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))
    indegree[b] += 1

start, end = map(int, input().split())

# start에서 각 도시까지 가는 최장 시간
dist = [0] * (n + 1)

# 위상정렬
q = deque()
q.append(start)

# start에서 출발 가능한 부분만 따라가도 됨
temp_indegree = indegree[:]

while q:
    now = q.popleft()

    for nxt, cost in graph[now]:
        if dist[nxt] < dist[now] + cost:
            dist[nxt] = dist[now] + cost

        temp_indegree[nxt] -= 1
        if temp_indegree[nxt] == 0:
            q.append(nxt)

# 역추적하면서 임계경로에 속한 간선 수 세기
count = 0
visited = [False] * (n + 1)
q = deque([end])
visited[end] = True

while q:
    now = q.popleft()

    for prev, cost in reverse_graph[now]:
        if dist[now] == dist[prev] + cost:
            count += 1
            if not visited[prev]:
                visited[prev] = True
                q.append(prev)

print(dist[end])
print(count)