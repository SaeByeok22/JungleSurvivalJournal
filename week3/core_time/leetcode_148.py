# leetcode 148

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # base case 기차가 한 칸 이하면 이미 정렬된 상태.
        if not head or not head.next:
            return head

        # 1. 리스트를 반으로 나누기
        slow, fast = head, head.next

        # slow는 한 칸만 가고, fast는 두 칸 가는애라, fast가 끝 까지 다 가면, slow가 간 만큼이 mid.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 중간 지점에서 리스트를 반으로 나누겟음.
        mid = slow.next
        slow.next = None  # 리스트 분리

        # 2. 재귀적으로 정렬 앞쪽, 뒤쪽 나눠두겟다.
        left = self.sortList(head)
        right = self.sortList(mid)

        # 3. 병합
        return self.merge(left, right)

    def merge(self, l1, l2):
        
        # 리스트 생성.. 빈 리스트 생성해서 나 머리다~~~ 하는 거.
        dummy = ListNode(0)
        
        # 현재 더미를 가리킴.
        current = dummy

        # l1과 l2가 잇음. 각 덩어리마다 남아잇는 동안 비교하겟다.
        # l1 = 4 / l2= 2
        while l1 and l2: 
            
            # l1보다 l2가 크다?
            if l1.val < l2.val:
                # 현재 dummy의 다음에 l1가 옴. 그리고 l1의 다음을 가리킴.
                current.next = l1
                l1 = l1.next
                
                # l1이 더 크면 dummy의 다음에 l2가 옴.
            else:
                current.next = l2
                l2 = l2.next

            # 새 기차의 끝을 한 칸 뒤로 이동함. 아직 붙이기 전의 next를 가리키고 있을거니깐... 붙고 나서의 next를 가리켜야지..
            current = current.next

        # 한 쪽 부분이 남았다? 남은 부분 연결
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next