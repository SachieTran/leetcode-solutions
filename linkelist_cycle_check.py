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
        if head == None:
            return False
            
        if head.next == None:
            return False
            
        slow_pointer = head
        fast_pointer = head
        
        while slow_pointer != None and fast_pointer != None:
            slow_pointer = slow_pointer.next
            if fast_pointer.next == None:
                break
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        
        return False
        