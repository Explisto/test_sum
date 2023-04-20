#https://leetcode.com/problems/search-a-2d-matrix/
def compare(matrix, num, index):
    
    if  num <= matrix[index][-1]:
        return matrix[index]
    
    elif index + 1 < len(matrix):
        return compare(matrix, num, index + 1)
    
def bin_search(data, num, left, right):

    mid = (right + left) // 2

    if data[mid] == num:
        return True

    if left > right:
        return False

    if data[mid] > num:

        return bin_search(data, num, left, mid - 1)

    else:

        return bin_search(data, num, mid + 1, right)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = compare(matrix,target, 0)
        
        if arr == None:
            return False
        
        return bin_search(arr, target, 0, len(arr) - 1)