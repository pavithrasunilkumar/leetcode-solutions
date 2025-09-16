class Solution(object):
    def trap(self, height):
   
        left, right = 0, len(height) - 1  # two pointers
        left_max, right_max = 0, 0        # max heights from both sides
        water = 0                         # total trapped water

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # update left max
                else:
                    water += left_max - height[left]  # water trapped
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # update right max
                else:
                    water += right_max - height[right]  # water trapped
                right -= 1

        return water
