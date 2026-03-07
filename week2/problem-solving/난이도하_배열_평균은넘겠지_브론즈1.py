# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# 문제 설명
# 첫째 줄에 테스트케이스 개수 C가 주어짐.
# 둘째 줄부터 각 테스트케이스마다 학생의 수(N)과, 각 학생의 점수가 주어짐.
# 각 테스트케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림해서 소수점 셋째 자리까지 출력함.
# 정답과 출력값의 절대오차가 10^-3 이하면 정답으로 인정함.

# 방법
# 테스트 케이스 개수 C를 입력받음
import sys
input = sys.stdin.readline
C = int(input())

# 각 테스트케이스마다 학생 수 N과 점수 리스트를 입력받음
for _ in range(C):
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]
    
# 각 줄 마다 평균 계산 후, 평균을 넘는 학생 수를 계산한다.
    avg = sum(scores) / N
    above_average_count = sum(1 for score in scores if score > avg)
    
# (평균을 넘는 학생 수 / 전체 학생 수) * 100을 계산하여 소수점 셋째 자리까지 출력한다.
    percentage = (above_average_count / N) * 100
    print(f"{percentage:.3f}%")