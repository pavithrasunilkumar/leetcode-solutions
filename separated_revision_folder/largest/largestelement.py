nums=[35, 12, 43, 8, 51, 27]
largest=float('-inf')
for i in range(len(nums)):
    if nums[i]>largest:
        largest=max(largest,nums[i])
        
    
print(largest,"is the largest")