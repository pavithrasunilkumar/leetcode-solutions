s=input("enter the input")
word=s.split()
result=[]

for i in word:
    char=list(i)
    left=0
    right=len(char)-1
    while left<right:
        char[left],char[right]=char[right],char[left]
        left+=1
        right-=1
        
    result.append("".join(char))
    
    
print("  ".join(result))