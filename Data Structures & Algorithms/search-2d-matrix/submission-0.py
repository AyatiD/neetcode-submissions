class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m - 1

        # Binary search to find the possible row
        while left <= right:
            row = (left + right) // 2

            if target < matrix[row][0]:
                right = row - 1

            elif target > matrix[row][n - 1]:
                left = row + 1

            else:
                # Target falls within this row's range
                break

        # No possible row
        if left > right:
            return False

        # Binary search inside the row
        row = (left + right) // 2
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False