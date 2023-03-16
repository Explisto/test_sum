#https://leetcode.com/problems/valid-palindrome-ii/
def ispal(s,l, r):
    while l<r:

        if s[l] != s[r]:
            return False

        l+=1
        r-=1

    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l<r:
            if s[l] != s[r]:
                return ispal(s,l+1, r) or ispal(s,l, r-1)
            
            l+=1
            r-=1

        return True