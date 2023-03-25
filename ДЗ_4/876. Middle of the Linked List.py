# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_slow = head
        current_fast = head

        if head == None or head.next == None:
            return head

        while current_fast and current_fast.next:
            
            if current_slow.next:
                current_slow = current_slow.next
            
            if current_fast.next:
                current_fast = current_fast.next
            
            if current_fast.next:
                current_fast = current_fast.next

        return current_slow
