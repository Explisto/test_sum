# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        list_ans = []
        j = 0
        
        while current:
            count+=1
            current = current.next
        
        current = head
        count_ans = count // 2 + 1
        while current:
            j+=1
            if (j == count_ans):
                break
            current = current.next
        return current