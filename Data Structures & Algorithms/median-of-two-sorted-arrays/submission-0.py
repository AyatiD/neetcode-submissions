class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A)

        while left <= right:
            # Number of elements taken from A
            i = (left + right) // 2

            # Number of elements taken from B
            j = half - i

            # Boundary values around the partitions
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total → median is the smallest right element
                if total % 2:
                    return min(Aright, Bright)

                # Even total → average of largest left and smallest right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Too many elements taken from A
            elif Aleft > Bright:
                right = i - 1

            # Too few elements taken from A
            else:
                left = i + 1