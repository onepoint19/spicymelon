# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        i = 0
        
        if head == None or head.next == None:
            return None
        while i < n:
            if p2.next != None:
                p2 = p2.next
            else:
                ans = head.next
                return ans
            i += 1
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        p2 = p1.next.next
        p1.next = p2
        return head
