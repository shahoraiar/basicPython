class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()

        count = 0
        for num in sorted(nums):
            if num in seen:
                # print(num)
                count += 1
            else:
                seen.add(num)

        # print(count)
        # print(type(count))
        nums.clear()
        nums.extend(list(seen))
        print(nums)
        return count
    
sol1 = Solution()
sol1.removeDuplicates([1,1,2])


