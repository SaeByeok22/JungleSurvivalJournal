# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []

# 입력 끝까지 받기
while True:
    try:
        preorder.append(int(input()))
    except:
        break


def postorder(start, end):
    if start > end:
        return

    root = preorder[start]

    # 오른쪽 서브트리 시작 지점 찾기
    mid = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            mid = i
            break

    # 왼쪽
    postorder(start + 1, mid - 1)
    # 오른쪽
    postorder(mid, end)
    # 루트 출력
    print(root)


postorder(0, len(preorder) - 1)