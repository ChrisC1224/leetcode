# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # print(2/10) 0.2
        # print(2//10) 0
        p = l1
        q = l2
        l3 = ListNode(0)
        res = l3
        sum = 0
        while p!=None or q!=None:
            sum //= 10
            if p!=None:
                sum += p.val
                p = p.next
            if q!=None:
                sum += q.val
                q = q.next
            res.next = ListNode(sum%10)
            res = res.next
        if sum//10 == 1:
            res.next = ListNode(1)
        return l3.next
