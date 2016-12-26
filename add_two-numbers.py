# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_ptr = l1
        l2_ptr = l2
        head = None
        current = None
        carry = 0
        while(l1_ptr!=None and l2_ptr!=None):
            val = l1_ptr.val + l2_ptr.val + carry
            carry = val//10
            val = val%10
            node = ListNode(val)
            if head == None:
                head = node
                current = head
            else:
                current.next = node
                current = node
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next
        
        if l1_ptr == None:
            while(l2_ptr != None):
                val = l2_ptr.val + carry
                carry = val//10
                val = val%10
                node = ListNode(val)
                current.next = node
                l2_ptr = l2_ptr.next
                current = node
        if l2_ptr == None:
            while(l1_ptr != None):
                val = l1_ptr.val + carry
                carry = val//10
                val = val%10
                node = ListNode(val)
                current.next = node
                l1_ptr = l1_ptr.next
                current = node
                
        if carry>0:
            node = ListNode(carry)
            current.next = node
        
        return head   
            
                
        