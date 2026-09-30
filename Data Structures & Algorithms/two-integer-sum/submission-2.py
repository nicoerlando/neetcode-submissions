class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}

        # 1. Map the difference to the index
        for i in range(len(nums)):
            diffMap[target - nums[i]] = i

        # 2. Find the match
        for j in range(len(nums)):
            # Check if the current number is a required difference for another number
            # AND ensure we aren't using the exact same index twice
            if nums[j] in diffMap and diffMap[nums[j]] != j:
                return [j,diffMap[nums[j]]]