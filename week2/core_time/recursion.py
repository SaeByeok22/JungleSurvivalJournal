# # 0부터 n까지 더하는 함수
# def nsum(n):
#     return sum([i for i in range(n + 1)])

# # return sum(list(range(n+1)))

# # recursion = 함수를 실행할 때에 함수 자기 자신을 또 호출하는 것...
# def rec_nsum(n):
#     if n == 0:
#         return 0 # 이걸 명시해줘야 함. base condition (이거 없으면 무한정 돌아감... n이 -1, -2, -3, ... )
#     return n + rec_nsum(n - 1)

# print(nsum(5))
# print(rec_nsum(5))

# # recursion 프로그래밍 시 rule들...
# # recursion 프로그래밍 시 중간에 break 하면 답을 못구함.,
# # recursion 프로그래밍 시에 base condition을 명시해줘야 함. 식에서의 변곡점 부분..


# # 이건 n이 0이 될 때 까지의 부분합을 출력하는 func.
# def sum_iter(n, total):
#     if n == 0:
#         return total
    
#     else:
#         return sum_iter(n-1, total + n)
    
# def sum(n):
#     return sum_iter(n, 0)
# # ? 변곡점이 없음!
# # 덧셈이나.. 그런게 없음. 이건 recursion 이긴 한데, tail recursion이라고 함.

# # 변곡점이 있는 rec는 변곡점(부메랑) 연산에 걸리는 시간이 2배 이벤트라면, tail rec는 변곡점이 없어서 덜 걸림.

# # exponentiation
# # b^0 = 1
# # b^n = b*b^n-1

# def exp(b, n):
#     if n == 0:
#         return 1
#     else:
#         return b * exp(b, n - 1)
    
# # 이걸 tail_recursion으로 구현해보자.

# # fast exponentiation
# # b^2 = b * b
# # b^4 = b^2 * b^2
# # ...

# def square(n):
#     return n * n

# def fexp(b, n):
#     if n == 0:
#         return 1
    
#     else:
#         if n % 2 == 0:
#             return square(fexp(b, n/2))
        
#         else:
#             return b * fexp(b, n - 1)
    
# # fast exponentiation - iteration으로 구현해보자.

# fibonacci num
from itertools import count


def fibonacci (n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# 얘는 트리구조...
# recursion이 그저 하나 더 늘었을 뿐인데 복잡해지고 overhead가 커짐...
# 왜냐구? 반복연산이니깐....
# 그럼 어떻게 최적화를 함?

# 만약 거스름돈을 줘야하는데.. 이걸 recursion으로 풀어야 한다면?
# if 금액은 4, 동전의 종류는 [1, 2 ,3] 라고 가정해보자.
# if.. 1을 제외하고 거슬러줄 수 있는 경우
# else.. 1을 넣어서 거슬러 줄 수 있는 경우의 수
#   ㄴ> 일단 1을 제외하구 생각함. 주어진 금액 3..으로.

def count_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    else:
        return count_change(amount, coins[1:]) + count_change(amount-coins[0], coins)
    
# hanoi tower...
# 대표적인 재귀...
# if 원판이 1개다? 바로 a to c
# else 원판이 두 개 이상이면..
def hanoi(n):
    
    # 원판이 없다? 리턴할 게 없음..
    if n == 0:
        return 0
    
    # 원판이 하나다? 
    if n == 1:
        return