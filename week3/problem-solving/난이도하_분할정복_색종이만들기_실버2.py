# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

#현재 정사각형이 한 색인지 검사
# -> 한 색이면 개수 증가
# -> 아니면 4등분 후 재귀

# 대충 로직..?
# 입력: N
# 입력: paper[N][N]

# white ← 0
# blue ← 0

# 함수 divide(x, y, size):

#     color ← paper[x][y]
#     same ← true

#     for i ← x to x + size - 1
#         for j ← y to y + size - 1
#             if paper[i][j] ≠ color
#                 same ← false
#                 break

#         if same = false
#             break

#     if same = true
#         if color = 0
#             white ← white + 1
#         else
#             blue ← blue + 1
#         return

#     half ← size / 2

#     divide(x, y, half)
#     divide(x, y + half, half)
#     divide(x + half, y, half)
#     divide(x + half, y + half, half)

# divide(0, 0, N)

# 출력 white
# 출력 blue

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def divide(x, y, size):
    global white, blue

    color = paper[x][y]
    same = True

    # 현재 영역이 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                same = False
                break
        if not same:
            break

    # 전부 같은 색이면 색종이 개수 증가
    if same:
        if color == 0:
            white += 1
        else:
            blue += 1
        return

    # 색이 섞여 있으면 4등분
    half = size // 2

    divide(x, y, half)                 # 왼쪽 위
    divide(x, y + half, half)          # 오른쪽 위
    divide(x + half, y, half)          # 왼쪽 아래
    divide(x + half, y + half, half)   # 오른쪽 아래

divide(0, 0, N)

print(white)
print(blue)