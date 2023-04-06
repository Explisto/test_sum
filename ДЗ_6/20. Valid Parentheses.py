#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        data = {"(":")",
                "{":"}",
                "[":"]"
                }

        for x in s:
            
            if x in data:
                st.append(x)
            
            else:
                if len(st) == 0 or data[st.pop()] != x:
                    return False

        
        if len(st) > 0:
            
            return False
        
        return True