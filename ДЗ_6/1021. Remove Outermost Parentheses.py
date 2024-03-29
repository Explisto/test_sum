#https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        count = 0
        stack = []

        for ch in s:

            if ch == "(":
                if count != 0:
                    stack.append(ch)
                count += 1
            
            elif ch == ")":
                count -= 1
                if count != 0:
                    stack.append(ch)

        return "".join(stack)