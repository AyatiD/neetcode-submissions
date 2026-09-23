class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []      # stores indices
        max_area = 0

        for i, h in enumerate(heights):

            # Current bar is smaller, so taller bars must stop here
            while stack and heights[stack[-1]] > h:
                height_index = stack.pop()
                height = heights[height_index]

                # Current i is the right boundary
                right = i

                # New stack top is the left boundary
                left = stack[-1] if stack else -1

                width = right - left - 1
                area = height * width

                max_area = max(max_area, area)

            stack.append(i)

        # Process bars that never found a smaller bar on the right
        n = len(heights)

        while stack:
            height_index = stack.pop()
            height = heights[height_index]

            right = n
            left = stack[-1] if stack else -1

            width = right - left - 1
            area = height * width

            max_area = max(max_area, area)

        return max_area