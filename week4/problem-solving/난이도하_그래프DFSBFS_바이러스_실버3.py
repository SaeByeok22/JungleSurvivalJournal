# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

n = int(input())      # 컴퓨터 수
m = int(input())      # 연결 수

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True
    for nxt in graph[x]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

print(sum(visited) - 1)