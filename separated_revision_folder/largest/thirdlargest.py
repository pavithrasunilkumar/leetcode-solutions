nums=[55,32,97,-55,45,32,88,21]
largest=float('-inf')
second=float('-inf')
third=float('-inf')

for i in range(len(nums)):
    if nums[i]> largest:
        third=second
        second=largest
        largest=nums[i]
        
    elif nums[i]>second and nums[i]!=largest:
        third=second
        second=nums[i]
        
    elif nums[i]>third:
        third=nums[i]
        
        
        
        
print("third largest ", third)
