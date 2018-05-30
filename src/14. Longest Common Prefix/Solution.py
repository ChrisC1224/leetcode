class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = strs[0]
        for i in strs[1:]:
            while len(res)>0 and res not in i[:len(res)]:
                res = res[:len(res)-1]
        return res
