#https://leetcode.com/problems/binary-search/
def bin_search(data, num, left, right):

  mid = (right+left) // 2

  if data[mid] == num:
    return mid

  if left > right:
    return -1

  if data[mid] > num:

    return bin_search(data, num, left, mid - 1)

  else:

    return bin_search(data, num, mid + 1, right)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bin_search(nums, target, 0, len(nums) - 1)