class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        largest,second,third=float('-inf'),float('-inf'),float('-inf')
        smallest,secondsmallest = float('inf'),float('inf')
        for i in range(len(nums)):
             if nums[i]>largest:
                third=second
                second=largest
                largest=nums[i]
             elif nums[i]>second:
                third=second
                second=nums[i]
             elif nums[i]> third:
                third=nums[i]
             
             if nums[i] < smallest:
                secondsmallest = smallest
                smallest = nums[i]

             elif nums[i] < secondsmallest:
                secondsmallest = nums[i]
        
        return int(max(largest*second*third ,smallest * secondsmallest * largest))
        