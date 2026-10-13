#method1 brute force tc=o(n+n/2) sc=o(n)
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


#optimal
nums=[-1,1,-2,2,-3,3]
n=len(nums)
result=[0]*n
pos=0
neg=1
for i in range(n):
    if nums[i]>0:
       result[pos]=nums[i]
       pos+=2
    else:
         result[neg]=nums[i]
         neg+=2
         
print(result)
        
        
    
