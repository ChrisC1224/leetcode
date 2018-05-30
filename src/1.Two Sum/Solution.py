class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, element in enumerate(nums):
            res = target - element
            if res in dic:
                i1 = dic.get(res)
                i2 = i
                break
            else:
                dic[element] = i
        return (i1,i2)
