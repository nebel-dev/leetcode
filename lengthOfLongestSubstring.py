class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk-i+1)
        return ans


res = Solution()
s = 'abcbca'
print("res:", res.lengthOfLongestSubstring(s))


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rk, ans = -1, 0
        occ = {}
        for i, element in enumerate(s):
            if element in occ and occ[element] > rk:
                rk = occ[element]  # meet a same element, then put the 'start' after this element
                occ[element] = i
            else:
                occ[element] = i
                ans = max(ans, i-rk)
        return ans


res2 = Solution2()
print("hashmap res2:", res2.lengthOfLongestSubstring(s))
