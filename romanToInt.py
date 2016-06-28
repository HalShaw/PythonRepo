class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for x in s[::-1]:
            res, p = res - d[x] if d[x] < d[p] else res + d[x], x#高位低于减去，高于加上
        return res