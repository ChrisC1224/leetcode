class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        left = []
        for i in s:
            if i == '}':
                if left and left[-1] == '{':
                    left.pop()
                else:
                    return False
            elif i == ']':
                if left and left[-1] == '[':
                    left.pop()
                else:
                    return False
            elif i == ')':
                if left and left[-1] == '(':
                    left.pop()
                else:
                    return False
            else:
                left.append(i)
        return left == []
                    
