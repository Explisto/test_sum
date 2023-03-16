class Solution:
	#https://leetcode.com/problems/reverse-string/
    def reverseString(self, s: List[str]) -> None:
        
        l_p = 0;
        r_p = len(s)-1
        sw = 0

        while (l_p < r_p):
            sw = s[l_p]
            s[l_p] = s[r_p]
            s[r_p] = sw
            l_p+=1
            r_p-=1
        
        return s