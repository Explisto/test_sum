#https://leetcode.com/problems/minimum-time-to-repair-cars/description/
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        left = 0
        right = min(ranks) * cars * cars

        while left < right:

            cars_speed = 0

            mid = (left + right) // 2
        
            for rank in ranks:

                cars_speed += math.floor((mid / rank) ** 0.5)

            if cars_speed < cars:

                left = mid + 1

            else:

                right = mid

        return left