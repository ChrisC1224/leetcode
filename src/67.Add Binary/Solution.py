class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a)
        j = len(b)
        while i < j:
            a = '0' + a
            i += 1
        while j < i:
            b = '0' + b
            j += 1
        flag = False
        res = ''
        while i:
            i -= 1
            if flag: # 有进位
                if (ord(a[i]) - ord('0')) ^ (ord(b[i]) - ord('0')):
                    res = '0' + res
                elif a[i] == '1' and b[i] == '1':
                    res = '1' + res
                else:
                    res = '1' + res
                    flag = False
            else:
                if (ord(a[i]) - ord('0')) ^ (ord(b[i]) - ord('0')):
                    res = '1' + res
                elif a[i] == '1' and b[i] == '1':
                    res = '0' + res
                    flag = True
                else:
                    res = '0' + res
        if flag == True:
            res = '1' + res
        return res
