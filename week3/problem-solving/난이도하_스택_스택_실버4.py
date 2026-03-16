# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stack.append(int(command[1]))

    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(stack))

    elif command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
            
# 람다식으로의 변환
# import sys

# input = sys.stdin.readline
# n = int(input())
# stack = []

# cmd = {
#     "pop": lambda: print(stack.pop() if stack else -1),
#     "size": lambda: print(len(stack)),
#     "empty": lambda: print(0 if stack else 1),
#     "top": lambda: print(stack[-1] if stack else -1)
# }

# for _ in range(n):
#     command = input().split()

#     if command[0] == "push":
#         stack.append(int(command[1]))
#     else:
#         cmd[command[0]]()