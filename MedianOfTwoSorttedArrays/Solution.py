class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=self._merge(nums1,nums2)
        length_nums=len(nums)
        if length_nums%2==1:
            return nums[int((length_nums+1)/2)-1]
        else:
            return (nums[int(length_nums/2)-1]+nums[int(length_nums/2)])/2.0

    def _merge(self,nums1, nums2):
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        length_nums1=len(nums1)-1
        length_nums2=len(nums2)-1
        nums=[]
        i=0
        j=0
        for k in range(length_nums1+length_nums2):
            if nums1[i]<=nums2[j]:
               nums.append(nums1[i])
               i+=1
            else:
               nums.append(nums2[j])
               j+=1
        return nums

if __name__=="__main__":
    nums1=[1,2]
    nums2=[3,4]
    s=Solution()
    print(s.findMedianSortedArrays(nums1,nums2))