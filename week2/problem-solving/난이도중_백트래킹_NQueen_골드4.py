# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

N = int(input())
# count = 0

used_col = [False] * N
used_diag1 = [False] * (2 * N - 1)
used_diag2 = [False] * (2 * N - 1)

def nqueen(row) :
    global count
    
    if row == N:
        return 1
    
    total = 0
    
    for col in range(N):
        diag1 = row - col + (N - 1)
        diag2 = row + col
        
        # if used_col[col]:
        #     continue
        # if used_diag1[diag1]:
        #     continue
        # if used_diag2[diag2]:
        #     continue
        if not used_col[col] and not used_diag1[diag1] and not used_diag2[diag2]:
            
            used_col[col] = True
            used_diag1[diag1] = True
            used_diag2[diag2] = True
            
            total += nqueen(row + 1)
            
            used_col[col] = False
            used_diag1[diag1] = False
            used_diag2[diag2] = False
            
    return total

print(nqueen(0))