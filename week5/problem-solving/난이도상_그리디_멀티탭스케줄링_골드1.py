# 그리디 - 멀티탭 스케줄링 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1700
n, k = map(int, input().split())
arr = list(map(int, input().split()))

plug = []
cnt = 0

for i in range(k):
    x = arr[i]

    if x in plug:
        continue

    if len(plug) < n:
        plug.append(x)
        continue

    idx = -1
    far = -1

    for p in plug:
        if p not in arr[i + 1:]:
            idx = p
            break
        next_use = arr[i + 1:].index(p)
        if next_use > far:
            far = next_use
            idx = p

    plug.remove(idx)
    plug.append(x)
    cnt += 1

print(cnt)