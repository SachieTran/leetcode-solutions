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
            return None
            
        if head.next == None:
            return None
            
        slow_pointer = head
        fast_pointer = head
        
        while slow_pointer != None and fast_pointer != None:
            slow_pointer = slow_pointer.next
            if fast_pointer.next == None:
                break
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return slow_pointer
        return None
        
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cycle_node = self.hasCycle(head)
        if cycle_node == None:
            return None
        
        # curr_ptr_check = head
        # while True:
        #     ptr2 = cycle_node
        #     while ptr2.next!=curr_ptr_check and ptr2.next!=cycle_node:
        #         ptr2 = ptr2.next
        #     if ptr2.next == curr_ptr_check:
        #         return ptr2.next
        #     curr_ptr_check = curr_ptr_check.next
        
        ptr1 = cycle_node
        ptr2 = cycle_node
        k = 1
        while(ptr1.next != ptr2):
            ptr1 = ptr1.next
            k += 1
        
        ptr1 = head
        ptr2 = head
        for i in range(k):
            ptr2 = ptr2.next
        
        while(ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1
            
        
        