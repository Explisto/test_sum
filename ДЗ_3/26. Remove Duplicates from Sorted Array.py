class Solution:
	#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    def removeDuplicates(self, nums: List[int]) -> int:
        left_p = 0
        count = 0
        for right_p in range(1, len(nums)):
            if nums[left_p] != nums[right_p]:
                 left_p+=1
                 nums[left_p] = nums[right_p]
                 count+=1
        
        return count+1
        return nums
