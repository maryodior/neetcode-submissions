class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem requires 1-indexed output
                return [left + 1, right + 1]
                
            elif current_sum < target:
                # Sum is too small, move left pointer to get a bigger number
                left += 1
                
            else:
                # Sum is too big, move right pointer to get a smaller number
                right -= 1

        