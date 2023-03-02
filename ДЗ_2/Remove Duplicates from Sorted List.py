# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        ds = 0
        if (current == None):
            return head
        list_ans = [current.val]
        while current.next:
            if (current.val != current.next.val):
                list_ans.append(current.next.val)
                count+=1
            current = current.next
        
        h = ListNode(list_ans[0])
        ans = h
        
        for i in list_ans[1:]:
            ans.next = ListNode(i)
            ans = ans.next
        
        return h