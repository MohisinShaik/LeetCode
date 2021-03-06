class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_frequency = {}
        maxLength, window_start = 0, 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if(right_char not in char_frequency):
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            while len(char_frequency) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if(char_frequency[left_char] == 0):
                    del char_frequency[left_char]
                window_start += 1
            maxLength = max(maxLength, window_end - window_start + 1)
        return maxLength
