s=input()
t=input()

if len(s)!= len(t):
    print(False)
    
freq={}
for char in s:
    freq[char]=freq.get(char,0)+1
    
for char in t:
    if char not in freq:
        print(False)
        
    freq[char]-=1
    
    if freq[char]<0:
        print(False)
        
print(True)
    

    

    

