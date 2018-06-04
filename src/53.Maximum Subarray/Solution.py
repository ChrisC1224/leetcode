class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sum = 0
        res = nums[0]
        for i in nums:
            Sum += i
            res = max(res, Sum)
            Sum = max(Sum, 0)
        return res
