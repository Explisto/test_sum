# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current_1 = list1
        current_2 = list2
        current = ListNode(0)
        head = current

        while current_1 and current_2:

            if current_1.val < current_2.val:
                current.next = current_1
                current_1 = current_1.next
                current = current.next
                
            else:
                current.next = current_2
                current_2 = current_2.next
                current = current.next
        
        while current_1:
            current.next = current_1
            current_1 = current_1.next
            current = current.next
        
        while current_2:
            current.next = current_2
            current_2 = current_2.next
            current = current.next

        return head.next
