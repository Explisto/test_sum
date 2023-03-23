# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bar = ""
        current = head

        while current:
            bar = bar + str(current.val)
            current = current.next
        
        return int(bar,2)