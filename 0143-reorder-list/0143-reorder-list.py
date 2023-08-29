# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        q=deque()
        node=head
        while node:             #insert elements of linked list into a queue
            node=node.next
            if not node:
                break
            q.append(node)
        
        while q:
            if head:            #pop last element from queue and insert in head.next
                temp=q.pop()
                head.next=temp
                head=head.next
            if head and q:      #pop first element from queue and insert in head.next
                temp=q.popleft()
                head.next=temp
                head=head.next
        head.next=None
        
