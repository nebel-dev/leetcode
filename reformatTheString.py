import itertools
import re


class Solution:
    def reformat(self, s: str) -> str:
        a = re.findall(r'\d', s)
        b = re.findall(r'[a-z]', s)
        if abs(len(a) - len(b)) > 1:
            return ''
        a, b = sorted([a, b], key=len)
        return ''.join(map(''.join, itertools.zip_longest(b, a, fillvalue='')))


str1 = "123abcd"
reformat1 = Solution
str2 = reformat1.reformat(str1)
print(str2)
