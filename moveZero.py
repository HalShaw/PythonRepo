class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x,y=0,0
        while x<len(nums):
            if nums[x]==0:
                x+=1
                continue
            else:
                nums[y],nums[x]=nums[x],nums[y]
            x+=1
            y+=1
    