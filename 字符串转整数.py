INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automation:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        """第一步，求初始start的状态，为下一个状态转移做准备"""
        """同时也是每一轮循环开始计算该字符所在状态的步骤"""
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(INT_MAX, self.ans) if self.sign == 1 else min(-INT_MIN, self.ans)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, s):
        automation = Automation()
        for c in s:
            automation.get(c)
        return automation.sign * automation.ans


res = Solution()
str = ' -2‬a'
a = res.myAtoi(str)
print(a)