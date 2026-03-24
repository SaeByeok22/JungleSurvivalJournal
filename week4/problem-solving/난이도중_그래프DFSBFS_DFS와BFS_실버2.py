# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for nxt in graph[x]:
        if not visited[nxt]:
            dfs(nxt)

def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

visited = [False] * (n + 1)
dfs(v)
print()

visited = [False] * (n + 1)
bfs(v)