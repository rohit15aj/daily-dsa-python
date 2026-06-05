class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to optimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = half_len - partition1
            
            # Identify border elements (handle out-of-bound edges with infinity)
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If combined length is odd
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # If combined length is even
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                    
            elif maxLeft1 > minRight2:
                # We took too many elements from nums1, shift left
                high = partition1 - 1
            else:
                # We took too few elements from nums1, shift right
                low = partition1 + 1
                
        return 0.0
