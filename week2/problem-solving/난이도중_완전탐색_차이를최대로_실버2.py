# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

# 완전 탐색 하는거면,,, 모든 조합을 다 봐야한다는건데..!!!
# 1. 입력한 숫자로 순열(배열) 조합함! -> 리스트로! permutations 이용
# 2. 덧셈 후 절댓값 계산 -> abs
# 3. 절댓값 계산한 값 다 더하기
# 4. 순열마다 다 계산해보는데, 합이 더 큰게 있다면 그 때 마다 값 갱신하기.

from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

max_num = 0
for perms in permutations(nums):
    total = 0
    for i in range(n - 1):
        total += abs(perms[i] - perms[i + 1])
    max_num = max(max_num, total)
    
print(max_num)

# 이렇게 하면 시간복잡도가 O(n * n!) 일텐데..?

# n = int(input())
# nums = list(map(int, input().split()))

# visited = [False] * n
# path = []
# answer = 0

# def dfs():
#     global answer

#     if len(path) == n:
#         total = 0
#         for i in range(n - 1):
#             total += abs(path[i] - path[i + 1])
#         answer = max(answer, total)
#         return

#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             path.append(nums[i])

#             dfs()

#             path.pop()
#             visited[i] = False

# dfs()
# print(answer)
# 이건 백트래킹으로 푼 거... 시간복잡도가 O(n * n!) 얘도 도찐개찐....