class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        largest=float('-inf')
        second=float('-inf')
        third=float('-inf')
        for i in range(len(nums)):
            if nums[i] == largest or nums[i] == second or nums[i] == third:
                continue
                
            if nums[i]> largest:
                third=second
                second=largest
                largest=nums[i]

            elif nums[i]>second and nums[i]!=largest:
                 third=second
                 second=nums[i]

            elif nums[i] > third and nums[i] != second:
                 third = nums[i]
                
        if third == float('-inf'):
            return largest


        return third
        
        
        
        

       