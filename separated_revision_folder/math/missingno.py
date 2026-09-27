a=[1,0,3,4,5]

n=len(a)
expected=n*(n+1)//2
actual=sum(a)

print("Missing number:", expected-actual)