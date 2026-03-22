# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline

n = int(input())

# 인접 리스트 (트리 저장)
graph = [[] for _ in range(n + 1)]

# 간선 입력 (양방향)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 부모를 저장할 배열
parent = [0] * (n + 1)

# DFS를 위한 스택 (루트 1부터 시작)
stack = [1]

# 스택 기반 DFS
while stack:
    now = stack.pop()
    
    # 현재 노드와 연결된 노드들 확인
    for nxt in graph[now]:
        # 아직 방문하지 않은 노드라면
        if parent[nxt] == 0 and nxt != 1:
            parent[nxt] = now  # 부모 기록
            stack.append(nxt)  # 다음 탐색 대상으로 추가

# 2번 노드부터 부모 출력
print(*parent[2:], sep='\n')