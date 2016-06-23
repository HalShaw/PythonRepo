class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]#nums1=[1,2,2,3],nums2=[2,2] 返回[2,2]
        lst=list(set(nums1)&set(nums2))#先求交集得出交集元素再统计元素个数添加到新列表
        for x in lst:
            if nums1.count(x)<nums2.count(x):
                c=nums1.count(x)
                for i in range(c):
                    l.append(x)
            else:
                c=nums2.count(x)
                for i in range(c):
                    l.append(x)
        return l

    