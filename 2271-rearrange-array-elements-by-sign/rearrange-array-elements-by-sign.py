class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        num=[0]*n
        pos,neg=0,1
        for i in nums:
            if i>=0:
                num[pos]=i
                pos+=2
            else:
                num[neg]=i
                neg+=2
        return num

        