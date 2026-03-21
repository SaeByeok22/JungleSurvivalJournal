# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
n, m = map(int, input().split())

# 1) 0 ~ (n-m+1)까지 경로 생성
for i in range(n - m + 1):
    print(i, i + 1)

# 2) 남은 정점들을 1번 정점에 붙이기
for i in range(n - m + 2, n):
    print(1, i)