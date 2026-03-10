# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

N = int(input())
count = 0

used_col = [False] * N
used_diag1 = [False] * (2 * N - 1)
used_diag2 = [False] * (2 * N - 1)

def nqueen(row) :
    global count
    
    if row == N:
        count = count + 1
        return
    
    for col in range(N):
        diag1 = row - col + (N - 1)
        diag2 = row + col
        
        if used_col[col] == True:
            continue
        if used_diag1[diag1] == True:
            continue
        if used_diag2[diag2] == True:
            continue
    
        used_col[col] = True
        used_diag1[diag1] = True
        used_diag2[diag2] = True
        
        nqueen(row + 1)
        
        used_col[col] = False
        used_diag1[diag1] = False
        used_diag2[diag2] = False
    
nqueen(0)
print(count)