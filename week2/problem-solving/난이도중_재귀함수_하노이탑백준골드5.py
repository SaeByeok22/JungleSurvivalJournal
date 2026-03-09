# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

# n 번째 원판을 옮기기 위해서는...
# n - 1 번째 원판까지 보조기둥에 잘 옮겨져 있어야 함.
# 그 다음에 n 번째 원판을 옮기고서 n - 1 번째 원판을 다시 도착기둥에 옮겨놔야 함...
# 근데, n이 20보다 큰 경우에는 과정은 출력할 필요가 없음. 그냥 이동 횟수만 출력하면 됨...
# 20까지는 과정 출력해야 하긴 함....
# 언제 다 해..?
n = int(input())
if n < 21:
    def hanoi(n, start, end, sub):
        if n == 1:
            print(start, end)
            return

        hanoi(n - 1, start, sub, end)
        print(start, end)
        hanoi(n - 1, sub, end, start)

    print(2**n - 1)
    hanoi(n, 1, 3, 2)

else:
    print(2**n - 1)