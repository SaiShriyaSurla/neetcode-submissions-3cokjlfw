class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        best = 0

        for right in range(len(s)):
            ch = s[right]

            while ch in charset:
                charset.remove(s[left])
                left = left +1
            charset.add(s[right])
            best = max(best, right - left +1)
        return best



        