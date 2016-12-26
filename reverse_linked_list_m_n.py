# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        curr = head
        counter = 1
        prev = None
        firstLink = None
        firstRLink = None
        lastLink = None
        while curr!=None and counter<=n:
            if counter>=m and counter!=n:
                if counter == m:
                    firstLink = prev
                    firstRLink = curr
                    prev = curr
                    curr = curr.next
                else:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
            elif counter==n:
                if firstLink!=None:
                    firstLink.next = curr
                firstRLink.next = curr.next
                temp = curr.next
                curr.next = prev
                if m==1:
                    head = curr
            else:
                prev = curr
                curr = curr.next
            counter+=1
        
        return head
        