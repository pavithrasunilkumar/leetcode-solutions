s=input("enter the string")
s = list(s)
right=len(s)-1
left=0


while left<right:
    if s[left]!=s[right]:
        print(" not a palindrome")
        break
        
    left += 1
    right -= 1
    
else:
    print("Palindrome")
        


"""
Complexity:
Time: O(n)
Space: O(1)

 """        