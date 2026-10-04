#method1 (tc=o(n) , sc=o(n))
nums=[1,0,7,0,3,12]
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
print(nums)


#method2 optimal(tc = o(n) , sc = o(1))
def moveZeroes(nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
