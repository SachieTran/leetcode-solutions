# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
            
        countA = 1
        ptr = headA
        while ptr.next!=None:
            ptr = ptr.next
            countA+=1
        countB = 1
        ptr = headB
        while ptr.next!=None:
            ptr = ptr.next
            countB+=1
        
        ptrA = headA
        ptrB = headB
        if countA>countB:
            k = countA - countB
            while k!=0:
                ptrA = ptrA.next
                k-=1
        elif countA<countB:
            k = countB - countA
            while k!=0:
                ptrB = ptrB.next
                k-=1
        
        while ptrA!=ptrB and ptrA!=None and ptrB!=None:
            ptrA = ptrA.next
            ptrB = ptrB.next
        
        if ptrA == None or ptrB == None:
            return None
        else:
            return ptrA
        
            
        
        