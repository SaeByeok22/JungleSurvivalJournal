# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

# 로직?
# N장의 카드를 1 ~ N까지 큐에 넣는다. [ 1 2 3 4 ]
# 가장 앞에 있는 카드(1)를 뺀다. [ 2 3 4 ]
# 2를 가장 아래로 옮긴다. [ 3 4 2 ]
# 3을 뺀다. [ 4 2 ]
# 4를 가장 아래로 옮긴다. [ 2 4 ]
# 2를 뺀다. [ 4 ]
# 가장 마지막에 남아있는 걸 출력한다.

from collections import deque

n = int(input())

queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft()              # 맨 앞 카드 버림
    queue.append(queue.popleft()) # 다음 카드 맨 뒤로 이동

print(queue[0])