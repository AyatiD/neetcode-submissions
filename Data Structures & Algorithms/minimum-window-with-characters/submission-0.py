class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # counting & storing frequency mapping of t
        count_t = {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # variables for s
        count_s = {}
        left = 0
        have = 0
        need = len(count_t)

        # variables for best window
        best_length = float('inf')
        best_left = 0
        best_right = 0

        # main loop
        for right in range(len(s)):

            char = s[right]
            count_s[char] = count_s.get(char, 0) + 1

            # checking individual requirement
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            # shrink while all requirements are satisfied
            while have == need:

                length = right - left + 1

                # save shortest valid window
                if best_length > length:
                    best_length = length
                    best_left = left
                    best_right = right

                # remove left character
                left_char = s[left]
                count_s[left_char] -= 1

                # check if removing it broke a requirement
                if left_char in count_t and count_s[left_char] < count_t[left_char]:
                    have -= 1

                left += 1

        if best_length == float('inf'):
            return ""

        return s[best_left:best_right + 1]