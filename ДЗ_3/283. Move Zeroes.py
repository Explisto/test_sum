class Solution:
	#https://leetcode.com/problems/move-zeroes/
    def moveZeroes(self, nums: List[int]) -> None:
        
        left_p = 0
        right_p = 0
        
        while right_p < len(nums):
            
            while nums[left_p] != 0 and left_p < right_p:
                left_p+=1
            
            if nums[right_p] != 0 and nums[left_p] == 0:
                nums[left_p] = nums[right_p]
                nums[right_p] = 0
                left_p+=1
            
            right_p+=1
            
        return nums