# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            nxt=curr.next    #store next value in
            curr.next=prev   #for first, prev will be none i.e. last elements next will be none.
            prev=curr
            curr=nxt
        return prev
