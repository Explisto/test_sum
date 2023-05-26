# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lo = 0
        hi = n

        while lo < hi:
            
            mid = (lo + hi) // 2
            
            if isBadVersion(mid) < True:
                lo = mid + 1
            else:
                hi = mid
        
        return lo