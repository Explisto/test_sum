# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        s_pol = ""
        while (current):
            s_pol = s_pol + str(current.val)
            current = current.next
        
        if (s_pol == s_pol[::-1]):
            return True
        else:
            return False