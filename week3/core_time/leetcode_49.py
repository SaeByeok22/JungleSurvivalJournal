# function groupAnagrams(strs):

#     hashmap = {}   # key : 정렬된 문자열, value : 문자열 리스트
#     for word in strs:
#         key = sort(word)   # 문자열 정렬
#         if key not in hashmap
#             hashmap[key] = []
#         hashmap[key].append(word)
#     return hashmap의 모든 value

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}

        for word in strs:
            key = ''.join(sorted(word))  # 문자열을 정렬해서 key 생성

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        return list(hashmap.values())        