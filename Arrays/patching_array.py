class Solution(object):
    def minPatches(self, nums, n):
        
        patches = 0
        i = 0
        miss = 1  # smallest number we cannot form yet

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # patch the array with 'miss'
                miss += miss
                patches += 1
        return patches
