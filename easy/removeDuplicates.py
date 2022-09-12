class Solution:
    def removeDuplicates(self, nums):
        #numbers = [nums[0]]
        #for idx in range(1, len(nums)):
        #    if nums[idx - 1] == nums[idx]:
        #        continue
        #    numbers.append(nums[idx])
        #return numbers
        nums[:] = sorted(set(nums))
        return nums

print(Solution().removeDuplicates([1,1,2]))