#https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
def bin_search(left, right, candies, kids, ans):

    if left > right:
        return ans

    mid = (left + right) // 2

    sum_candies = 0

    for elem in candies:
        sum_candies += elem // mid

    if sum_candies >= kids:

        if ans < mid:

            return bin_search(mid + 1, right, candies, kids, mid)

        else:

            return bin_search(mid + 1, right, candies, kids, ans)
            
    else:

        return bin_search(left, mid - 1, candies, kids, ans)

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        return bin_search(1, max(candies), candies, k, 0)