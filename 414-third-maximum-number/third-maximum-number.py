class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=float("-inf")
        second=float("-inf")
        third=float("-inf")

        for num in nums:
            if first==num or second==num or third==num:
                continue

            if num>first:
                third=second
                second=first
                first=num
                

            elif num>second:
                third=second
                second=num

            elif num > third:
                third = num

        if third == float('-inf'):
            return first

        return third



        