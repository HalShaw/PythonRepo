class Solution(object):#简单版
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = n
        while(result > 10):
            result = 0
            while(n > 0):
                i = n % 10
                n = n/10
                result+=pow(i,2)
            n=result
        if n==7:
            return True
        elif n==10:
            return True
        elif n==1:
            return True
        return False

class Solution(object):#进阶版
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n!=1:
            if n in visited:
                return False
            visited.add(n)
            n = reduce(lambda x,y:x+y,(map(lambda x:int(x)**2,list(str(n)))))
        return True
