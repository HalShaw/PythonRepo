'''class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        right = 0
        while (right < n):
        	if (nums[right]):
        		nums[left] = nums[right]
        		left+=1
        	right+=1
        while (left < n):
        	left+=1
        	nums[left]=0

if __name__ == '__main__':
	s=Solution()
	print(s.moveZeroes([1,0,20,0,1]))

enumerate'''
words=["abcw","baz","foo","bar","xtfn","abcdef"]
l=[]
for i in range(len(words)):
    for j in range(1,len(words)):
        print(set(words[i]),set(words[j]))
        if not set(words[i])&set(words[j]):
            s=len(words[i])*len(words[j])
            l.append(s)
print(max(l))
