s=input("enter the string")
s = list(s)
right=len(s)-1
left=0


while left < right:
    s[left], s[right] = s[right], s[left]
    left+=1
    right-=1
    
print("".join(s))