class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Input: 
                           i   l
        nums1 = [10,20,20,40,0,0], m = 4,
                   j 
        nums2 = [1,2], n = 2

        Output: [1,2,10,20,20,40]
        """
        last = m + n - 1
        i = m - 1 # nums1
        j = n - 1 # nums2

        while j >= 0:
            if i >= 0 and nums2[j]<nums1[i]:
                nums1[last]= nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1

        
            
        