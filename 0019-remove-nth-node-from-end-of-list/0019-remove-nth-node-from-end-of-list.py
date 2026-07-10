# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self,head,n):
        d=ListNode(0)
        d.next=head
        f=d
        s=d
        for _ in range(n+1):
            f=f.next
        while f:
            f=f.next
            s=s.next
        s.next=s.next.next
        return d.next
        