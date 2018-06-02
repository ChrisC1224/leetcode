class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in nums:
            if nums[j]!=i:
                j+=1
                nums[j] = i
        return j+1
