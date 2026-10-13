class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive=[]
        negative=[]
        for x in nums:
            if x > 0:
                positive.append(x)
            else:
                negative.append(x)
        num=nums
        for i in range(len(positive)):
            num[i*2]=positive[i]
            num[(i*2)+1]=negative[i]

        return num

        