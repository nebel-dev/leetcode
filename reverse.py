class Solution:
    def reverse(self, x: int) -> int:
        INTMAX = (2**31)-1
        INTMIN = -(2**31)
        rev = 0
        while x!=0:
            pop = -(abs(x)%10) if x<0 else x%10
            x = -(abs(x)//10) if x<0 else x//10
            if rev > INTMAX // 10 or (rev == INTMAX // 10 and pop >7):
                return 0
            if rev < -(abs(INTMIN)//10)or (rev == -(abs(INTMIN)//10) and pop <-8):
                return 0
            rev = rev * 10 + pop
        return rev


res = Solution()
print(res.reverse(-123))


class Solution2:
    def reverse(self, x: int) -> int:
        negative_flag = 1
        if x < 0:
            x = abs(x)
            negative_flag = -1
        res = tmp = 0
        while x:
            tmp = x % 10  # 取余
            x = x//10  # 取整
            res = res*10 + tmp  #
        result = negative_flag*res  # 添加符号
        return result if -2**31 < result < 2**31-1 else 0


res2 = Solution2()
print(res2.reverse(2147483647))