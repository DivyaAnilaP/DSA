class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for idx,num in enumerate(nums):
            comp=target-num
            if comp in di:
                return [di[comp],idx]
            di[num]=idx