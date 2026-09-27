nums=list(map(int,input("enter").split()))

seen=set()
duplicate=[]
for num in nums:
    if num in seen:
        if num not in duplicate:
            duplicate.append(num)
            
    else:
        seen.add(num)
print("Duplicate elements:", duplicate)