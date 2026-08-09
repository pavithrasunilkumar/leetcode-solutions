class Solution:
    def reverse(self, x: int) -> int:
        negative= x<0
        num=abs(x)
        digits = list(str(num))
        left = 0
        right = len(digits) - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1
        result = int("".join(digits))
        if negative:
            result= -result
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
        