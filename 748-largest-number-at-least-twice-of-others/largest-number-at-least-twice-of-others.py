class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest=float('-inf')
        second=float('-inf')
        index=-1

        for i in range(len(nums)):
            if nums[i]>largest:
                second=largest
                largest=nums[i]
                index=i

            elif nums[i]>second and largest!=nums[i]:
                second=nums[i]


        if largest>= 2*second:
            return index

        return -1      