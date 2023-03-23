# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        current_A = headA
        current_B = headB
        l_A = 0
        l_B = 0
        count = 0

        while current_A:
            l_A += 1
            current_A = current_A.next
        
        while current_B:
            l_B += 1
            current_B = current_B.next
        
        current_A = headA
        current_B = headB
        
        if l_A < l_B:
            count = l_B - l_A
            while count > 0:
                current_B = current_B.next
                count -= 1
        
        elif l_A > l_B:
            count = l_A - l_B
            while count > 0:
                current_A = current_A.next
                count -= 1

        while current_A:
            if current_A == current_B:
                return current_A
            
            current_A = current_A.next
            current_B = current_B.next
        
        return None