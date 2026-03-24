# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    color = [0] * (v + 1)
    ok = True

    for i in range(1, v + 1):
        if color[i]:
            continue

        q = deque([i])
        color[i] = 1

        while q and ok:
            x = q.popleft()
            for nx in graph[x]:
                if color[nx] == 0:
                    color[nx] = -color[x]
                    q.append(nx)
                elif color[nx] == color[x]:
                    ok = False
                    break

        if not ok:
            break

    print("YES" if ok else "NO")