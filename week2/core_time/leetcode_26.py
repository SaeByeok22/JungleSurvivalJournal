class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1
    
# 자바로 하면 이 모양임.    
# class Solution {
#     public int removeDuplicates(int[] nums) {
#         int j = 0;
#         for (int i = 1; i < nums.length; i++) {
#             if (nums[j] != nums[i]) {
#                 nums[++j] = nums[i];
#             }
#         }
#         return ++j;
#     }
# }