class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
	#https://leetcode.com/problems/intersection-of-two-arrays/
        p_1 = 0
        p_2 = 0
        p_3 = 0
        rez = []
        flag = False
        call = False

        while p_1 < len(nums1):

            while p_2 < len(nums2):
                
                if nums1[p_1] == nums2[p_2]:
                    flag = True
                
                p_2+=1
            
            if flag == True:
                
                while p_3 < len(rez):
                    if rez[p_3] == nums1[p_1]:
                        call = True
                    p_3+=1
                
                if call == False:
                    rez.append(nums1[p_1])
            
            flag = False
            call = False
            p_1 += 1
            p_2 = 0
            p_3 = 0
    
        return rez