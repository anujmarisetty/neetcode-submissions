class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in nums:
                idx=nums.index(comp)
                if i!=idx:
                    return sorted([i,idx])