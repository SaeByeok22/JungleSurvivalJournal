# 백트래킹 - 비숍 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1799

# Hint! 짝 홀 분리해서 back tracking!

# N과 체스판 상태(0/1)로 입력함.
# (r + c)%2로 체스판 흑/백 구분.  
# 흑/백 각각 각 색에 놓을 수 있는 비숍의 최대 개수 판별. 
#   ㄴ> if 비숍을 뒀다면, 해당 대각선 값(r + c/r - c)에는 모두 1 -> 0
# 0을 제외한 1만 있는 곳에만 비숍을 둠.
# 비숍을 다 두면 사용된 비숍의 수 리턴..
# 더 큰 값이 나오면 갱신하다가, 흑 최대 비숍 수 + 백 최대 비숍 수 리턴 후 프린트.

n=int(input())
g = [list(map(int, input().split())) for _ in range(n)]

visit1 = [0]*(2 * n - 1)
visit2 = [0]*(2 * n - 1)
queens = [];cnt=0; max_ = 0
def bishop(k):
    global cnt, max_
    check = 0
    max_ = max(max_,cnt)
    if k == 2 * n - 1:
        return
    for j in range(k + 1):
        if 0 <= k - j < n and 0 <= j < n:
            if g[k - j][j]==1:
                a = k - 2 * j + n - 1; b = k
                if not visit1[a] and not visit2[b]:
                    check += 1
                    visit1[a] = 1; visit2[b] = 1
                    cnt += 1
                    bishop(k + 1)
                    cnt -= 1
                    visit1[a] = 0; visit2[b] = 0
    if not check:
        bishop(k + 1)
bishop(0)
print(max_)