class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n :
            k = n // 5
            count += k
            n = k
        return count
                
        