class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = dict()
        for i in range(len(nums)):
            if target - nums[i] in idxs.keys():
                return [idxs[target-nums[i]], i]
            idxs[nums[i]] = i