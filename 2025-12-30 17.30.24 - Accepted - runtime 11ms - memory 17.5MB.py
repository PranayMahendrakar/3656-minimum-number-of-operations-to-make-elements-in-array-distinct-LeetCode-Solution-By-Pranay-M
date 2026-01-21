class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        while len(nums) > 0 and len(nums) != len(set(nums)):
            nums = nums[3:]  # Remove first 3 elements
            ops += 1
        return ops