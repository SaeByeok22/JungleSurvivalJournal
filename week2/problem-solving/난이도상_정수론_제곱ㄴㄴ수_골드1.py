# 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1016

# 두 정수 min과 max를 띄어쓰기로 구분해 입력받음.
# 길이 max - min + 1 인 배열 생성.
# i^2 <= max 인 수를 추림.
# 추려진 제곱수로 배수를 만들어 리스트에 집어넣음.
# Min 부터 Max 까지, 리스트에 있는 수와 비교한 뒤에, 해당하는 수가 있다면 True로 변환.

min, max = map(int, input().split())

length = max - min + 1
is_square_multiple = [False] * length

i = 2
while i * i <= max:
    square = i * i

    start = ((min + square - 1) // square) * square

    for j in range(start, max + 1, square):
        is_square_multiple[j - min] = True

    i += 1

count = 0
for x in is_square_multiple:
    if not x:
        count += 1

print(count)