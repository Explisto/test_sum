#https://leetcode.com/problems/make-the-string-great/
class Solution:
    def makeGood(self, s: str) -> str:

        stack = []
        
        for ch in s:

            if stack and ((ord(ch)) == (ord(stack[-1]) + 32) or (ord(ch) + 32) == (ord(stack[-1]))):
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)