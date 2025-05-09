# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            # print(num)
            if num in seen:
                print(num)
                return True
            else:
                seen.add(num)
        return False

sol1 = Solution()
sol1.containsDuplicate([1,2,3,1])