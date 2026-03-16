# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

# 시작 위치 (1, 1)에 뱀 놓기.
# 현재 방향은 (2, 0) (오른쪽)
# 시간은 변수로 관리. time += 1이 됨에 따라 for문 돌림.
#   시간 + 1...:
#   -> 머리의 다음 위치 계산
#   -> 벽 / 몸 충돌 -> 현재 time return
#   -> 다음 칸 머리 이동
#   -> if 사과 o -> 사과를 제거함.
#   -> else -> 꼬리를 제거함.
#   -> if 현재 시각이 방향을 전환할 시각이면? 회전함.

# 입력 N -> N * N 보드 생성
# 입력 K -> 사과 갯수 입력
#   ㄴ> 사과 위치. (행, 열)
# 입력 L -> 뱀의 방향 전환 횟수
#   ㄴ> 시간 X, 문자 C 입력. X는 time을, C는 L(왼) 또는 D(오) 둘 중 하나임.

# snake = deque 생성
# snake에 (1,1) 추가          # 시작 위치

# board[1][1] = SNAKE

# direction = RIGHT
# time = 0

# 반복 시작 (무한 루프)

#     time = time + 1
#     head = snake의 마지막 위
#     next = head를 direction 방향으로 1칸 이동

#     만약 next가 보드 밖이면
#         게임 종료
#         break

#     만약 next가 SNAKE이면
#         게임 종료
#         break

#     snake에 next 추가

#     만약 board[next] == APPLE 이면
#         사과 제거
#         (꼬리 유지 → 길이 증가)

#     아니면
#         tail = snake의 맨 앞 제거
#         board[tail] = EMPTY

#     board[next] = SNAKE

#     만약 time이 turn_info에 존재하면
#         turn_direction = turn_info[time]

#         만약 turn_direction == 'L'
#             direction = 왼쪽 회전

#         만약 turn_direction == 'D'
#             direction = 오른쪽 회전

# 반복 종료
# time 출력

from collections import deque #얘는 아무래도 앞 뒤 다 뺄 수 있는 deque가 필요할듯.
import sys

input = sys.stdin.readline
N = int(input())
board = [[0]*(N+1) for _ in range(N+1)] # 보드 생성

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1     # 사과 생성
    
L = int(input())
turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

# 방향이 어뜨케 되는지. . .?
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

snake = deque()
snake.append((1, 1))
board[1][1] = 2  # 뱀의 초기 위치

time = 0  # 시간 변수 생성...

while True:
    time += 1
    
    head_x, head_y = snake[-1]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]
    
    if nx < 1 or nx > N or ny < 1 or ny > N or board[nx][ny] == 2:
        print(time)
        break
    
    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.append((nx, ny))
    
    else:
        board[nx][ny] = 2
        snake.append((nx, ny))
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
        
    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4