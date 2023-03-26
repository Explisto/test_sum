# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        current_1 = headA
        current_2 = headB
        flag = True

        if headA == None or headB == None:
            return None

        while current_1 and current_2:

            current_1 = current_1.next
            current_2 = current_2.next

            if current_1 == None and flag:
                flag = False
                current_1 = headA

                while current_2:
                    headB = headB.next
                    current_2 = current_2.next
            
            if current_2 == None and flag:
                flag = False
                current_2 = headB
                
                while current_1:
                    headA = headA.next
                    current_1 = current_1.next
        
        current_1 = headA
        current_2 = headB

        while current_1 and current_2:

            if current_1 == current_2:
                return current_1
            
            current_1 = current_1.next
            current_2 = current_2.next
        
        return None
