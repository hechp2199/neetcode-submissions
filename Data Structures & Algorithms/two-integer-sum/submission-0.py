class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen = {}
        i=0
        for i in range(len(nums)):
            if target-nums[i] in seen:
                return [seen[target-nums[i]], i]
            else:
                seen[nums[i]]=i