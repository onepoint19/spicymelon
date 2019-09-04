# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.swapRecur(None,None,head)
        
    def swapRecur(self,prehead,pretail,head):
        if head == None or head.next == None:
            if prehead != None:
                return prehead
            return head
        a = head
        b = a.next
        
        if pretail == None:
            a.next = b.next
            b.next = a
            return self.swapRecur(b,a,a.next)
        if pretail != None:
            pretail.next = b
            a.next = b.next
            b.next = a
            return self.swapRecur(prehead,a,a.next)
