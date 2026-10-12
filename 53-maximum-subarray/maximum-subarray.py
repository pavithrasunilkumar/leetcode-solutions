class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        total=0
        maximum=float("-inf")
        for i in range(0,n):
            total=total+nums[i]
            maximum=max(total,maximum)
            if total<0:
                total=0
        return maximum