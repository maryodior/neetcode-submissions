class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: list[int] = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j and nums[i] == nums[j]:
                    continue
                if nums[i] + nums[j] == target:
                    result.extend([i, j])
                    result.sort()
                    return result
        
        