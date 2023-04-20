#https://leetcode.com/problems/peak-index-in-a-mountain-array/
def bin_search(data, mid):

    if data[mid] > data[mid - 1] and data[mid] > data[mid + 1]:

        return mid

    if data[mid] > data[mid - 1]:

        return bin_search(data, mid + 1)

    else:

        return bin_search(data, mid - 1)


class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        return bin_search(arr, (len(arr) - 1) // 2)