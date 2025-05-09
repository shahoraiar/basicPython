# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0  
        # print(nums) 
        for num in nums:
            # print(len(str(num)))
            if len(str(num)) % 2 == 0 :
                count += 1

        # print(count)
        return count

sol1 = Solution()
sol1.findNumbers([12,345,2,6,7896])
