class Solution:
    def twoSum(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []

print(Solution().twoSum([2, 7, 11, 15], 18))
