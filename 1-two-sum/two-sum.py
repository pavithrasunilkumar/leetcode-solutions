class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        n=len(nums)
        for i in range(0,n):
            complement=target-nums[i]
            if complement in seen:
                return (seen[complement],i)
            seen[nums[i]]=i
        

        
        