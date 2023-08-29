# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        pos=0
        l=0
        while curr:
            l+=1
            curr= curr.next
        pos=l-n-1
        l=0
        curr=head

        if pos==-1:
            return head.next
        while curr:
            if l==pos:
                curr.next=curr.next.next
                break
            curr=curr.next
            l+=1
        return head