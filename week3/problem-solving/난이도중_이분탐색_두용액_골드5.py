# 이분탐색 - 두 용액 (백준 골드5)
N = int(input())
a = sorted(map(int, input().split()))
l, r = 0, len(a)-1
ans = (a[l], a[r])

while l < r:
    s = a[l] + a[r]
    if abs(s) < abs(ans[0] + ans[1]):
        ans = (a[l], a[r])
    if s > 0:
        r -= 1
    else:
        l += 1

print(*ans)