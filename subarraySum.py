class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq=defaultdict(int)
        freq[0]=1
        prefix,ans=0,0
        for num in nums:
            prefix+=num
            ans+=freq.get(prefix-k,0)
            freq[prefix]+=1
        return ans
