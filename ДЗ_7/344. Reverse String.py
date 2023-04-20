#https://leetcode.com/problems/reverse-string/
def check(s, left, right):
    if left > right:
        return s
    s[left], s[right] = s[right], s[left]
    return check(s, left + 1, right - 1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        s = check(s, left, right)