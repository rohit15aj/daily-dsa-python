lass Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            # If character is repeated and within the current window
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            
            # Update the last seen index of the character
            char_map[s[end]] = end
            
            # Calculate the max length found so far
            max_length = max(max_length, end - start + 1)
            
        return max_length

        
