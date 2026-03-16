# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

m = int(input())

for _ in range(m):
    command = input().split()

    if command[0] == 'L':
        if left:
            right.append(left.pop())

    elif command[0] == 'D':
        if right:
            left.append(right.pop())

    elif command[0] == 'B':
        if left:
            left.pop()

    elif command[0] == 'P':
        left.append(command[1])

print(''.join(left + right[::-1]))