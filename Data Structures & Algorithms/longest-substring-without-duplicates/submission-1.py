class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        # 'right' moves across the string character by character
        for right in range(len(s)):
            # If we find a duplicate, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the max length found so far
            current_window_len = right - left + 1
            if current_window_len > max_length:
                max_length = current_window_len
                
        return max_length
        