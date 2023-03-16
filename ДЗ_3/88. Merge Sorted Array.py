class Solution:
    #https://leetcode.com/problems/merge-sorted-array/
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        sw = 0
        flag = True

        while p1 >= 0 and p2 >= 0:
            
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]

        return nums1