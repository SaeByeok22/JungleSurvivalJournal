# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

N,M = map(int, input().split())

parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA  # 합치기

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

# 연결 요소 개수 계산
roots = set()
for i in range(1, N + 1):
    roots.add(find(i))

print(len(roots))