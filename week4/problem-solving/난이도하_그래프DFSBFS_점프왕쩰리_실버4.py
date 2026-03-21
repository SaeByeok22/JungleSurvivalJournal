# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
answer = False

def dfs(x, y):
    global answer

    if answer:
        return

    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if visited[x][y]:
        return

    visited[x][y] = True

    if board[x][y] == -1:
        answer = True
        return

    jump = board[x][y]

    dfs(x + jump, y)
    dfs(x, y + jump)

dfs(0, 0)

print("HaruHaru" if answer else "Hing")