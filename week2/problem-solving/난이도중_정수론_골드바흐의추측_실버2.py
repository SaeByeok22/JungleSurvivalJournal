# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

# 문제 설명
# 골드바흐란? 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 이론.
# 10000이하의 모든 짝수 n에 대한 골드바흐 파티션은 존재함.
# 2보다 큰 짝수 n의 골드바흐 파티션을 출력하는 프로그램 작성해라.
# 단, 작은 것부터 먼저 출력하고, 공백으로 구분함.
# 그리고 여러 파티션이 있다면, 그 격차가 가장 작은 것을 출력할 것.
# 4 = 2 + 2
# 6 = 3 + 3
# 8 = 3 + 5
# ...

# 일단 이건 기본으로 깔고 감...
import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


t = int(input())

nums = []
for _ in range(t):
    nums.append(int(input()))

for n in nums:
    a = n // 2
    b = n // 2

    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b += 1