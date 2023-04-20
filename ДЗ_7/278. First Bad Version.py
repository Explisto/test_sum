#https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def bin_search(left, right):

    mid = (left + right) // 2

    if left > right:
        return left
    
    if not isBadVersion(mid):
        return bin_search(mid + 1, right)

    else:
        return bin_search(left, mid - 1)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return bin_search(1, n)