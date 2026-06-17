class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()  # You already nailed this step!
        
        for i in range(len(nums) - 2):
            # Skip the exact same value for 'i' to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # If the lowest possible number is greater than 0, 
            # three positive numbers can never add up to 0. Stop early!
            if nums[i] > 0:
                break
                
            # Initialize two pointers for the rest of the array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers forward/backward after a match
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < 0:
                    # Sum is too small, make it bigger by moving left pointer
                    left += 1
                else:
                    # Sum is too big, make it smaller by moving right pointer
                    right -= 1
                    
        return triplets


        