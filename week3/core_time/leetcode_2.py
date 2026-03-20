# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        num1 = 0  # 첫 번째 리스트를 숫자로 바꿔 저장할 변수
        num2 = 0  # 두 번째 리스트를 숫자로 바꿔 저장할 변수
        mul = 1   # 현재 자릿값(1의 자리, 10의 자리, 100의 자리...)을 나타내는 변수

        # l1 → 숫자로 변환!
        while l1:  # l1이 끝날 때까지 반복
            num1 += l1.val * mul  # 현재 노드 값을 해당 자릿값과 곱해서 num1에 더함
            mul *= 10  # 다음 자리로 넘어가기 위해 자릿값을 10배로 키움
            l1 = l1.next  # 다음 노드로 이동

        mul = 1  # 두 번째 리스트를 변환할 때 다시 1의 자리부터 시작하도록 초기화

        # l2 → 숫자로 변환!
        while l2:  # l2가 끝날 때까지 반복
            num2 += l2.val * mul  # 현재 노드 값을 해당 자릿값과 곱해서 num2에 더함
            mul *= 10  # 다음 자리로 넘어가기 위해 자릿값을 10배로 키움
            l2 = l2.next  # 다음 노드로 이동

        total = num1 + num2  # 두 숫자를 더해서 최종 합을 구함

        # 전환된 숫자 → 리스트
        dummy = ListNode(0)  # 결과 리스트의 시작을 쉽게 만들기 위한 더미 노드
        cur = dummy  # 현재 결과 리스트의 마지막 노드를 가리킬 포인터

        if total == 0:  # 합이 0이면
            return ListNode(0)  # 0 하나만 가진 노드를 바로 반환

        while total > 0:  # total의 각 자리를 꺼낼 수 있는 동안 반복
            cur.next = ListNode(total % 10)  # 1의 자리 숫자를 새 노드로 만들어 뒤에 연결
            cur = cur.next  # 현재 포인터를 새로 만든 노드로 이동
            total //= 10  # 1의 자리를 제거하고 다음 자리로 넘어감

        return dummy.next  # 더미 노드 다음부터가 진짜 결과 리스트이므로 반환