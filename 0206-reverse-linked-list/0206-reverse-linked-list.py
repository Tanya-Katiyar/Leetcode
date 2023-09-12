# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # iterative
        prev,curr=None,head
        # while curr:
        #     nxt=curr.next    #store next value in
        #     curr.next=prev   #for first, prev will be none i.e. last elements next will be none.
        #     prev=curr
        #     curr=nxt
        # return prev

        #recursive
        def reverse(prev,curr):
            if not curr:
                return prev
            temp=curr.next
            curr.next=prev
            return reverse(curr,temp)
        return reverse(None,head)
        

