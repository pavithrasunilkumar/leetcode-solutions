class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        Sum=n*(n+1)//2
        actual=sum(nums)
        return (Sum-actual)