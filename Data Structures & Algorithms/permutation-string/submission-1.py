class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}

        # Count frequencies in s1
        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        left = 0

        for right in range(len(s2)):

            # Add the new character to the window
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            # If window becomes too large, remove from the left
            if right - left + 1 > len(s1):
                count2[s2[left]] -= 1

                # Remove key if its frequency becomes 0
                if count2[s2[left]] == 0:
                    del count2[s2[left]]

                left += 1

            # Check if current window is a permutation of s1
            if count1 == count2:
                return True

        return False