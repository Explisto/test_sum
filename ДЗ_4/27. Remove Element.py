class Solution
    #https://leetcode.com/problems/remove-element/
    def removeElement(self, nums List[int], val int) - int
        p_1 = 0
        p_2 = len(nums)-1

        while p_1 = p_2

            while nums[p_2] == val
                p_2 -= 1
                
                if p_2 == -1
                    return 0
            
            if p_1  p_2
                return p_1
            
            if nums[p_1] == val
                nums[p_1] = nums[p_2]
                nums[p_2] = val
                p_2 -= 1
                
            p_1 += 1
        
        return p_1