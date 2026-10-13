class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        num=[0]*n
        pos=0
        neg=1
        for i in range(n):
            if nums[i]>=0:
                num[pos]=nums[i]
                pos+=2
            else:
                num[neg]=nums[i]
                neg+=2
        return num

        