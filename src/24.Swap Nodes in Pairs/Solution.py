# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # p = ListNode(0)
        # p.next = head
        # head = p
        # while p.next and p.next.next:
        #     q = p.next
        #     r = q.next
        #     p.next = r
        #     q.next = r.next
        #     r.next = q
        #     p = p.next.next
        # return head.next
        
        # recursion 
        if(head==None or head.next==None):
            return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head
        return temp
