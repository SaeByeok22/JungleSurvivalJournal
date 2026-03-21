# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # 비어있는 트리면 깊이는 0
        if root is None:
            return 0
        
        # 비어있지 않다면...
        ## 왼쪽 트리의 최대 깊이 구하기.
        left_depth = self.maxDepth(root.left)

        ## 오른쪽 트리의 최대 깊이 구하기.
        right_depth = self.maxDepth(root.right)
        
        # 현재 노드 포함해서 더 깊은 쪽 선택. 여기서 1이 카운터 역할을 함.
        return 1 + max(left_depth, right_depth)
    
# self를 쓰는 이유?
# 여기서 maxDepth는 클래스 안에 있는 함수임. 
# 같은 클래스 안에서 다시 부르기 위해서는 이 객체의 solution 인스턴스인 self를 함께 써줘야함.
# 그래야 이 객체 안에 있는 함수임을 파이썬이 인지함. 
# 만약 self를 쓰지 않는다..? 어디 소속인지 몰라서 에러가 뜸.

# 재귀 특성상 맨 아래부터 시작함. 
# if 15..를 보자. left = 0, right = 0이니깐, return 1 + max (0, 0)으로 깊이가 1임.
# 7도 똑같음.
# 그럼 20을 보자. left = 1(15), right = 1(7)이니깐, return 1 + max (1, 1)로 깊이가 1 + 1 = 2임.
# 9는 리프니깐 1
# 마지막으로 루트 노드인 3.. left = 1(9), right = 2(20)이니깐, return 1 + max (1, 2)로 깊이가 1 + 2 = 3임.

# 즉, 이 코드의 구조는 리프에서 시작해서 위로 올라오며 1씩 더하는 거임.!