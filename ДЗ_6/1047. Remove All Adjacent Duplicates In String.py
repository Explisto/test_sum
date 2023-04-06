#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        
        for x in range(len(s)):
            
            if len(stack) == 0 or stack[-1] != s[x]:
                stack.append(s[x])
            
            else:
                stack.pop()
        
        return ''.join(stack)