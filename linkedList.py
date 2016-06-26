# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first=head
        second=head
        while second and second.next:
            first=first.next
            second=second.next.next
            if first is second:#判断地址用is
                return True
        return False
      