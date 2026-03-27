# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline  # 입력을 빠르게 받기 위한 설정 (대량 입력 대비)

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    N = int(input())  # 지원자 수
    
    # 지원자들의 (서류 순위, 면접 순위)를 리스트로 저장
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    
    # 서류 성적 기준으로 오름차순 정렬
    # (파이썬은 tuple의 첫 번째 값 기준으로 자동 정렬됨)
    arr.sort()
    
    # 첫 번째 지원자는 무조건 뽑힌다
    # (비교 대상이 없기 때문)
    count = 1
    
    # 현재까지 본 사람 중 면접 순위의 최소값 (가장 좋은 면접 성적)
    min_interview = arr[0][1]
    
    # 두 번째 지원자부터 끝까지 확인
    for i in range(1, N):
        
        # 현재 지원자의 면접 순위가 더 좋다면 (숫자가 더 작다면)
        if arr[i][1] < min_interview:
            
            # 선발 가능
            count += 1
            
            # 최소 면접 순위를 갱신
            min_interview = arr[i][1]
    
    # 최종 선발 인원 출력
    print(count)