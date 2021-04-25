class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # one-pass, count the previous and current group of 0 or 1's
        prev_count = 0
        curr_group_letter = s[0]
        curr_count = 1
        ans = 0
        for c in s[1:]:
            if c == curr_group_letter:
                curr_count += 1
            else:
                curr_group_letter = c
                prev_count = curr_count
                curr_count = 1
            if curr_count <= prev_count:
                ans += 1
        return ans

sol = Solution()
print(sol.countBinarySubstrings("11001100"))
