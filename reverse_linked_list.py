# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
            
        prev = None
        curr = head
        
        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head