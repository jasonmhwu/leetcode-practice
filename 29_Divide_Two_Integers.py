class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # handle the sign upfront, so we only need to deal with positive numbers
        # use a stack to keep track of divisor, 2*divisor, ....
        # will need O(log Y/x) time, O(log Y/x) space
        if dividend == 0:
            return 0
        neg_sign = False
        if dividend < 0 and divisor < 0:
            return self.divide(-dividend, -divisor)
        if dividend < 0 or divisor < 0:
            neg_sign = True
            dividend, divisor = abs(dividend), abs(divisor)

        ans = 0
        multiplier = [divisor]
        idx = [1]
        while True:
            if not multiplier:
                break
            if dividend - multiplier[-1] >= 0:
                dividend -= multiplier[-1]
                ans += idx[-1]
                multiplier.append(multiplier[-1] + multiplier[-1])
                idx.append(idx[-1] + idx[-1])
            else:
                multiplier.pop()
                idx.pop()
        if neg_sign:
            ans = -ans
        if ans < -2**31 or ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans
            
sol = Solution()
print(sol.divide(10, 3))
print(sol.divide(1, 1))
print(sol.divide(0, 1))
print(sol.divide(7, -3))
print(sol.divide(-20, -6))
print(sol.divide(2147483647, -1))
print(sol.divide(-2147483648, 1))
