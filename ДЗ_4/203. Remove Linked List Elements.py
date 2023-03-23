# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        current = head

        if head == None:
            return head
        
        while current and current.val == val:
            head = current.next
            current = head
        
        if current:
            while current.next:
                
                if current.next.val == val:
                    current.next = current.next.next
                else:
                    current = current.next
        
        return head