#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        max = 0
        
        for ch in s:
            
            if ch is "(":
                
                stack.append(ch)
                
                if len(stack) > max:
                    max = len(stack)
            
            elif ch is ")":
                stack.pop()

        return max