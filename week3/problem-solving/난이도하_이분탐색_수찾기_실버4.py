# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
# binary search?

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

for t in targets:
    print(binary_search(A, t))
    
    
    
# A = set(map(int, input().split()))

# for t in targets:
#     if t in A:
#         print(1)
#     else:
#         print(0)
# 이렇게도 가능은 함...