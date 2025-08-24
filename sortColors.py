class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_idx=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min_idx]:
                    min_idx=j
            nums[min_idx],nums[i]=nums[i],nums[min_idx]
        return nums
