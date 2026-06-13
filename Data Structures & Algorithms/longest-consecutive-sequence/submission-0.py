class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tempArray = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i, value in enumerate(nums):
            if i == len(nums) - 1:
                if nums[i] - nums[i - 1] == 1:
                    tempArray.append(nums[i])
                    break
                    
            if nums[i + 1] == value:
                continue
            elif nums[i + 1] - value == 1:
                tempArray.append(value)
                continue
            elif nums[i + 1] - value > 1:
                tempArray.append(nums[i - 1])
                break
            else:
                break
            
        return len(tempArray)



        