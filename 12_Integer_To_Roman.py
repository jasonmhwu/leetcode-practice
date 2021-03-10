class Solution:
    def intToRoman(self, num: int) -> str:
        def digitToRoman(digit: int, c1: str, c2: str, c3: str) -> str:
            """convert digit to a roman string."""
            
            if digit <= 3:
                return c1 * digit
            elif digit == 4:
                return c1 + c2
            elif digit <= 8:
                return c2 + (digit-5) * c1
            else:
                return c1 + c3
        
        ans = ''
        modulo = 10
        while num > 0:
            digit = num % modulo
            if modulo == 10:
                ans = digitToRoman(digit * 10 // modulo, 'I', 'V', 'X') + ans
            elif modulo == 100:
                ans = digitToRoman(digit * 10 // modulo, 'X', 'L', 'C') + ans
            elif modulo == 1000:
                ans = digitToRoman(digit * 10 // modulo, 'C', 'D', 'M') + ans
            else:
                ans = digitToRoman(digit * 10 // modulo, 'M', '', '') + ans
            num -= digit
            modulo *= 10
        return ans

sol = Solution()
print(sol.intToRoman(3))         
print(sol.intToRoman(4))         
print(sol.intToRoman(3827))         
print(sol.intToRoman(382))         
print(sol.intToRoman(96))         
