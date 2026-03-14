# / 기준으로 경로를 잘라서 조각들을 본다.
#         각 조각을 앞에서부터 처리하면서
#         ""(빈 문자열) 이나 . 이면 무시 
#         .. 이면 스택에서 하나 꺼내기
#         그 외는 정상 디렉토리 이름이므로 스택에 넣기
        
#         스택 stack 생성
#         path를 '/' 기준으로 나눈 리스트 parts 생성

#         parts의 각 요소 part에 대해 반복:

#             만약 part == "" 또는 part == "." 이면
#                 계속 (무시)

#             아니고 part == ".." 이면
#                 만약 stack이 비어있지 않으면
#                     stack에서 pop

#             아니면
#                 stack에 part push

#         만약 stack이 비어있으면
#             "/" 반환

#         아니면
#             "/" + stack을 "/"로 join 한 문자열 반환

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # 빈 스택 생성.
        stack = []
        # / 기준으로 나누기.
        parts = path.split("/")

        # parts 리스트의 각 요소를 part에 하나씩 넣어 반복
        for part in parts:

            # 빈 문자열("") 또는 "." 은 경로 변화가 없으므로 무시한다.
            if part == "" or part == ".":
                continue

            # 만약 ..이다? 부모 디렉토리로 가기 때문에.. 그간 쌓인 스택에다가 pop을해서 돌아감...
            elif part == "..":
                if stack:
                    stack.pop()

            # 그 외의 경우(..., .... 포함) 일반 디렉토리 이름이면 stack에 추가
            else:
                stack.append(part)
    
        # stack에 저장된 디렉토리들을 /로 연결하여 최종 경로 생성
        # .join(stack)이 스택에 쌓인 문자열을 하나하나 합치는 역할. (/home/이렇게 출력하기 위해 "/"을 하나 더 씀.)
        return "/" + "/".join(stack)