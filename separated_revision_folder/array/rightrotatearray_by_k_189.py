#brute force (TC=O(R*N)  , SC=O(1))
nums=[3,9,5,6,7,2]
n=len(nums)
k=int(input("no,of rotation?"))
rotation=k%n
for _ in range(0,rotation):
    e=nums.pop()
    nums.insert(0,e)
    
    
#slicing( TC=O)
def rotate(self, nums: list[int], k: int) -> None:
       n=len(nums)
       k=k%n
       nums[:]=nums[n-k:]+nums[:n-k]
       
       
#reverse
def rotate(self, nums: list[int], k: int) -> None:

        n = len(nums)
        k = n%k

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(n-k, n-1)
        reverse(0, n-k-1)
        reverse(0, n-1)