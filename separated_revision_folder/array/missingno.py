a=[1,0,3,4,5]



#method1 OPTIMAL (TC = O(n) , SC = O(1))
n=len(a)
expected=n*(n+1)//2
actual=sum(a)

print("Missing number:", expected-actual)


#method2 (TC = O(n) , SC = O(n))
nums=[1,0,3,4,5]
freq={}
for i in range(0, len(nums)):   #dict created
    freq[i]=0
for num in nums:                #changed freq in dict
    freq[num]=1
for k,v in freq.items():        #checking missing number
    if v==0:
        print("Missing number:",k)