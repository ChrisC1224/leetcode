class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        temp = x
        res = 0
        # while x != 0:
        #     res = res * 10 + x % 10
        #     x //= 10
        # if temp == res:
        #     return True
        # else:
        #     return False
        while res < x:
            res = res * 10 + x % 10
            if res == x:
                break
            x //= 10
        if res == x:
            return True
        else:
            return False
