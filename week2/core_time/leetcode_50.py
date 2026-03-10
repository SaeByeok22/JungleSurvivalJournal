class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        # n 이 음수인 경우....
        if n < 0:
            x = 1 / x
            
            # n을 양수화 함.
            n = -n
        
        # 곱셈 누적할라고 1로 둠.    
        result = 1
        
        # n이 양수면..? 
        while n > 0:
            
            # 그 n이 홀수라면..
            if n % 2 == 1:
                
                # 지수가 홀수라면 현재의 x를 결과에 곱한다.
                # x ^ n = x * x ^ (n - 1) 꼴이기 때문...
                # 2 ^ 5 = 2 × 2 ^ 4 처럼 표현
                result *= x
            
            # x를 제곱한다.    
            # 2 → 4 → 16 → 256 ...
            x *= x
            
            # 지수를 절반으로 줄임.
            # n = 10 → 5 → 2 → 1 → 0
            n //= 2
        
        # 계산된 x ^ n 값을 반환함.
        return result