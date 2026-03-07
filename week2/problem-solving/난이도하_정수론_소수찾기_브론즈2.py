# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

# 문제 설명
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하자.
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1000이하의 자연수이다.
# 주어진 수들 중 소수의 개수를 출력한다.

# 방법
# 첫 줄에 개수 N을 입력받는다.
import sys
import math
input = sys.stdin.readline
N = int(input())

# 그 다음 줄에 N개의 수가 주어진다. 수는 1000이하의 자연수이다.
nums = list(map(int, input().split()))

# count 변수를 만든다.
count = 0

# 첫 번째 수 부터 소수인지 아닌지 판별한다.
    # 1이면 소수가 아님
    # 2부터 √n까지 나눠보는데, 하나라도 나누어 떨어지면 소수가 아님.
    # 끝까지 나눠지지 않으면 소수다.
    # count를 1 증가시킨다.
for num in nums:
    if num == 1:
        continue
    
    is_prime = True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print(count)