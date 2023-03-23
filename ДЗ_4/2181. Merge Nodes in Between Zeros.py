# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/merge-nodes-in-between-zeros/
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_1 = head
        current_2 = head
        rez = 0
        sw = 0
        ls = []

        while current_1:
            
            while current_1.val != 0:
                rez = rez + current_1.val
                current_1 = current_1.next
            
            current_1 = current_1.next
            
            if rez != 0:
                ls.append(rez)
                rez = 0
        
        while sw < len(ls):
            current_2.val = ls[sw]
            if sw == len(ls) - 1:
                current_2.next = None
            else:
                current_2 = current_2.next
            sw += 1
    

        return head