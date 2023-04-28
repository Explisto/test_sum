#https://leetcode.com/problems/koko-eating-bananas/
def bin_search_bananas(left, right, h, piles):
    
    elem = 0
    mid = (right + left) // 2
    h_bananas = 0
    ans = right

    if left > right:
        
        return left

    for elem in piles:

        h_bananas += math.ceil(elem / mid)
    
    if h_bananas <= h:

        return bin_search_bananas(left, mid - 1, h, piles)
    
    else:

        return bin_search_bananas(mid + 1, right, h, piles)



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        return bin_search_bananas(1, max(piles), h, piles)