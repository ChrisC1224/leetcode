class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        # length = 0
        # l = len(s)-1
        # while s[l] == ' ' and l >= 0:
        #     l -= 1
        # while s[l] != ' ' and l >= 0:
        #     length += 1
        #     l -= 1
        # return length
        a = s.split()
        if a == []:
            return 0
        return len(a[-1])
