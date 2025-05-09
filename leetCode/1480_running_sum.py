# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution: 
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_num = list()
        sum = 0
        for num in nums:
            # print(num)
            sum = sum + num
            sum_num.append(sum)
        # print(sum_num)
        return sum_num
    
sol1 = Solution()
sol1.runningSum([1,2,3,4])

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

