class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 아무런 문자열도 받지 않으면 빈 리스트를 반환하라.
        if not digits:
            return []

        phone = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        def dfs(idx, path, output):
            if idx == len(digits):
                output.append(path)
                return
            letters = phone.get(digits[idx], "")
            for ch in letters:
                dfs(idx + 1, path + ch, output)

        result = []
        dfs(0, "", result)
        return result


if __name__ == "__main__":
    print(Solution().letterCombinations("12"))
