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
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lst=sorted(list(set(nums)))
        for i,x in enumerate(lst):
            if target<lst[0]:
                return 0
            elif x==target:
                return i
            elif target>lst[-1]:
                l=len(lst)
                return l
            else:
                while target<x:
                    target=x
                    return i
if __name__=='__main__':
    s=Solution()
    print(s.searchInsert([1,2,3,4,5,6,8],7))