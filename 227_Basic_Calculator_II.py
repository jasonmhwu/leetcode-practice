class Solution:
    def calculate(self, s: str) -> int:
        # O(n) time and space
        stack = [0]
        s += '*'
        for char in s:
            if char == ' ':
                continue
            elif char.isnumeric():
                stack[-1] = stack[-1]*10 + int(char)
            else:
                if len(stack) >= 3 and stack[-2] in ['*', '/']:
                    num2 = stack.pop()
                    operator = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1*num2 if operator == '*' else int(num1 / num2))
                stack.append(char)
                stack.append(0)
        ans = stack[0]
        for i in range(1, len(stack)-2, 2):
            ans += stack[i+1] if stack[i] == '+' else -stack[i+1]
        return ans
        
sol = Solution()
print(sol.calculate('2*2 + 3*3'))
