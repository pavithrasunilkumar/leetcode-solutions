class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        temp=[]
        n1=len(nums)
        for i in range(0,n1):
            if nums[i]!=0:
                temp.append(nums[i])
        n2=len(temp)
        for i in range(0,n2):
            nums[i]=temp[i]
        for i in range(n2,n1):
            nums[i]=0
        