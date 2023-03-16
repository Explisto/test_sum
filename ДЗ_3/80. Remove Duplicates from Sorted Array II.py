class Solution:
    #https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
    def removeDuplicates(self, nums: List[int]) -> int:

        p1 = 0
        p2 = 2

        if len(nums) < 3:
            return len(nums)
        

        for p1 in range(2, len(nums)):
            
            if nums[p1] != nums[p2-2]:
                nums[p2] = nums[p1]
                p2 += 1
        
        return p2