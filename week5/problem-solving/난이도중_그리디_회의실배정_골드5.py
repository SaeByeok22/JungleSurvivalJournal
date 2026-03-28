# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간 우선, 같으면 시작 시간 기준 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0

for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)