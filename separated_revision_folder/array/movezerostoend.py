 #method1
 
nums=[0,1,0,3,12]
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