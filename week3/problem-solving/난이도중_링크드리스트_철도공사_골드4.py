# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
stations = list(map(int, input().split()))

prev = {}
next = {}

# 원형 연결 리스트 초기화
for i in range(n):
    prev[stations[i]] = stations[i - 1]
    next[stations[i]] = stations[(i + 1) % n]

for _ in range(m):
    cmd = input().split()

    if cmd[0] == "BN":
        i, j = int(cmd[1]), int(cmd[2])
        ni = next[i]
        print(ni)

        next[i] = j
        prev[j] = i
        next[j] = ni
        prev[ni] = j

    elif cmd[0] == "BP":
        i, j = int(cmd[1]), int(cmd[2])
        pi = prev[i]
        print(pi)

        next[pi] = j
        prev[j] = pi
        next[j] = i
        prev[i] = j

    elif cmd[0] == "CN":
        i = int(cmd[1])
        ni = next[i]
        print(ni)

        nni = next[ni]
        next[i] = nni
        prev[nni] = i

    elif cmd[0] == "CP":
        i = int(cmd[1])
        pi = prev[i]
        print(pi)

        ppi = prev[pi]
        prev[i] = ppi
        next[ppi] = i