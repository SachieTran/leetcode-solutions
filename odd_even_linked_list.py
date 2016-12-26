# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        odd = head
        even = head.next
        evenFirst = head.next
        
        while True:
            if not odd or not even or not even.next:
                odd.next = evenFirst
                break
            
            odd.next = even.next
            odd = even.next
            
            if odd.next == None:
                even.next = None
                odd.next = evenFirst
                break
            
            even.next = odd.next
            even = odd.next
        
        return head
        