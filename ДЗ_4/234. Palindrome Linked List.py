# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        current_slow = head
        current_fast = head

        if head == None or head.next == None:
            return True
        
        while current_fast and current_fast.next:
            
            current_slow = current_slow.next

            if current_fast.next:
                current_fast = current_fast.next.next
        
        current_1 = head
        current_2 = current_slow
        next_p = None
        prev = None

        while current_2:
            next_p = current_2.next
            current_2.next = prev
            prev = current_2
            current_2 = next_p
        
        current_1 = head
        current_2 = prev

        while current_1 and current_2:
            
            if current_1.val != current_2.val:
                return False
            
            current_1 = current_1.next
            current_2 = current_2.next
        
        return True
