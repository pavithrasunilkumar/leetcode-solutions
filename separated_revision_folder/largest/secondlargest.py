nums=[55,32,97,-55,45,32,88,21]
largest=float('-inf')
second=float('-inf')

for i in range(len(nums)):
    if nums[i]> largest:
        second=largest
        largest=nums[i]
        
    elif nums[i]>second and nums[i]!=largest:
        second=nums[i]
        
print("second largest ", second)
