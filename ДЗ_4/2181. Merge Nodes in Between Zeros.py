# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/merge-nodes-in-between-zeros/
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current_1 = head.next
        current_2 = head
        rez = 0

        while current_1:

            while current_1.val != 0:
                rez += current_1.val
                current_1 = current_1.next
            
            current_2.next = current_1
            current_2.next.val = rez
            current_1 = current_1.next
            current_2 = current_2.next
            rez = 0
        
        return head.next
