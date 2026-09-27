s=input()
p=input()

if len(p) > len(s):
    return []

result=[]
p_freq = {}
window = {}

for char in p:
    p_freq[char] = p_freq.get(char, 0) + 1
    
left=0
for right in range(len(s)):
    char
    
