class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # base case
        if n == 1:
            return 1

        # 계단 1개인 경우 
        a = 1
        # 계단이 두 개인 경우
        b = 2

        for _ in range (3, n + 1):
            a, b = b, a + b

        return b