# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

# 문제 설명:
# 문자열 S를 입력받은 후, 각 문자를 R번 반복해 새 문자열 P를 만든다.
# 첫번째 문자를 R번.. 두번째 문자를 R번.. 이런식으로 반복한다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.

# 방법
# 숫자와 문자열을 순차적으로 입력 받는다.
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)

# 배열 각 번호에 있는 문자를 R번 반복하여 새로운 문자열 P에 추가한다.
    # P = ''
    # for s in S:
    #     P += s * R 
    # print(P)
    
    # 이게 더 나을라나..?
    print(''.join(c * R for c in S))
    

