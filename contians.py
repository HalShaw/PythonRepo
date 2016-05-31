class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=[]
        l2=[]
        for x in s:
            l1.append(x)
            if x in ['a','e' ,'i','o','u','A','E' ,'I','O','U']:
                l2.append(x)
        revl=l2[::-1]
        j=0
        for i,y in enumerate(l1):
            if y in ['a','e' ,'i','o','u','A','E' ,'I','O','U']:
                l1[i]=revl[j]
                j+=1
        res=''.join(l1)
        return res