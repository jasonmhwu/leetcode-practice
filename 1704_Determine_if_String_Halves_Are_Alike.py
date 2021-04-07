class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # O(n) time, O(n) space
        isVowel = [1 if c in ['a', 'e', 'i', 'o', 'u'] else 0 for c in s.lower()]
        return sum(isVowel[:len(s)//2]) == sum(isVowel[len(s)//2:])

sol = Solution()
print(sol.halvesAreAlike("Book"))
print(sol.halvesAreAlike("BoOk"))
