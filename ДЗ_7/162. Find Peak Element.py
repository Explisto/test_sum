#https://leetcode.com/problems/find-peak-element/
def bin_search(data, mid):

    if len(data) == 1:
        return 0
    
    if len(data) == 2:

        if data[0] > data[1]:
            return 0
        else:
            return 1
    
    if data[-1] > data[-2]:
        return len(data) - 1
    
    if data[mid] > data[mid - 1] and data[mid] > data[mid + 1]:

        return mid

    if data[mid] > data[mid - 1]:

        return bin_search(data, mid + 1)

    else:

        return bin_search(data, mid - 1)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return bin_search(nums, len(nums) // 2)