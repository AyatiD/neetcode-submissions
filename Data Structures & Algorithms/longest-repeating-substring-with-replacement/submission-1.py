class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_length = 0
        max_freq = 0

        for right in range(len(s)):
            # Add current character to the window
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency of any character in the window
            max_freq = max(max_freq, count[s[right]])

            # Characters we need to replace
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Current valid window length
            max_length = max(max_length, right - left + 1)

        return max_length