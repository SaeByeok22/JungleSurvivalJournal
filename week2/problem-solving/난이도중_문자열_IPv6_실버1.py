# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

# 문제 풀이
# 일단 문자열(최대 39자)을 받음.
# 콜론(::)이 있는지 확인!
# 있다면..
# -> 좌 우 분리
# -> 좌 우 각각 그룹 리스트 만들기
# -> 부족한 0의 개수 채우기. (전체 그룹 8에서 있는 것만 빼면 부족한 개수가 나옴!)
# 없다면.. 그냥 콜론 기준 분리
# 모든 그룹을 4자리 수로 만들기
# 콜론 붙여서 출력함.
ipv6 = input().strip()

if "::" in ipv6:
    left, right = ipv6.split("::", 1)
    left_parts = left.split(":") if left else []
    right_parts = right.split(":") if right else []
    parts = left_parts + ["0000"] * (8 - len(left_parts) - len(right_parts)) + right_parts
else:
    parts = ipv6.split(":")

parts = [part.zfill(4) for part in parts]

print(":".join(parts))