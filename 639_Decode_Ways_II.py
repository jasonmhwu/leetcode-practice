class Solution:
    def numDecodings(self, s: str) -> int:
        # use dp solution
        # should take O(n) time and O(1) space
        
        dp = [0, 1]
        for idx in range(len(s)):
            ans = 0
            # one character case
            if s[idx] == '*':
                ans += dp[-1] * 9
            elif 1 <= int(s[idx]) <= 9:
                ans += dp[-1]
            else:
                pass
            
            if idx == 0:
                dp[0], dp[1] = dp[1], ans % (10**9  + 7)
                continue
            # two character case
            if s[idx-1] == '*':
                if s[idx] == '*':
                    ans += dp[-2] * 15
                elif int(s[idx]) <= 6:
                    ans += dp[-2] * 2
                else:
                    ans += dp[-2]
            elif s[idx-1] == '0':
                pass
            elif s[idx-1] == '1':
                ans += dp[-2] * (9 if s[idx] == '*' else 1)
            elif s[idx-1] == '2':
                if s[idx] == '*':
                    ans += dp[-2]*6
                elif int(s[idx]) <= 6:
                    ans += dp[-2]
                else:
                    pass
            else:
                pass
            
            dp[0], dp[1] = dp[1], ans % (10**9  + 7)
        return dp[-1]
