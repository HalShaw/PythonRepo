class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        elif n==3:
            return 2
        elif n==4:
            return 4
        else:
            count=0
            while n>1:
                n=n-3
                count+=1
                if n==2:
                    return 3**count*2
                    break
                elif n==4:
                    return 3**count*4
                    break
                elif n==0:
                    return 3**count
                    break
                else:
                    continue
                