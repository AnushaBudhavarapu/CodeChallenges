#intersection of two arrays
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        lst=[]
        longer=nums1 if len(nums1)>nums2 else nums2
        shorter=nums2 if len(nums2)>nums1 else nums1
        for i in longer:
            if i in shorter:
                lst.append(i)
        return lst
