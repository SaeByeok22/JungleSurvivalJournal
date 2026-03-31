class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        # 일단 bottom up 방식으로 풀어야 할 거 같은데..
        # 일단 아래 줄을 시작 값으로 읽어옴..
        dp = triangle[-1][:]
        
        # 일단 아래에서 위로 올라감. 근데 맨 아래에서 한줄 위(6, 5, 7)부터 시작하겟다.
        for row in range(len(triangle) -2, -1, -1):
            for i in range(len(triangle[row])):
                # 현재 값 + 아래 두 값 중에 작은 값..
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])

        return dp[0]