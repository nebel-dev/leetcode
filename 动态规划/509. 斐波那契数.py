"""
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3

提示：0 <= n <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 时间复杂度：O(2^n), 存在大量重复计算
    # 自底向上
    def fib(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)

    # 可以用数组或哈希表（字典）记录要重复计算的节点值
    # 带备忘录的递归解法，自顶向下
    # 时间复杂度：O(n)
    def fib_memo(self, n: int) -> int:
        def fib(vals: dict, n):
            if n == 1 or n == 2:
                return 1
            if n in vals:
                return vals[n]
            vals[n] = fib(vals, n-1) + fib(vals, n-2)
            return vals[n]
        if n < 1:
            return 0
        vals = {}
        return fib(vals, n)

    # 使用DP数组
    # 时间复杂度：O(n)
    def fib_dp_array(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        dp_array = []
        dp_array.append(0)
        dp_array.append(1)
        dp_array.append(1)
        for i in range(3, n+1):
            dp_array.append(dp_array[i-1] + dp_array[i-2])
        return dp_array[n]

    # 考虑到每次只用到前两个计算结果，抛弃数组，使用两个中间值
    # 空间复杂度：O(n) -> O(1)
    def fib_state_compression(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        prev = curv = 1
        for i in range(3, n+1):
            sumv = prev + curv
            prev = curv
            curv = sumv
        return curv

    # 矩阵快速幂
    # 时间复杂度：O(log(n))
    def fib_matrix_power_series(self, n: int) -> int:
        if n < 2:
            return n
        q = [[1, 1], [1, 0]]
        res = self.matrix_pow(q, n-1)
        return res[0][0]

    def matrix_pow(self, a: List[List[int]], n: int) -> List[List[int]]:
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ret = self.matrix_multiply(a, ret)
            n >>= 1
            a = self.matrix_multiply(a, a)
        return ret

    def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c


if __name__ == "__main__":
    solution = Solution()
    # ans = solution.fib(20)
    # print("ans :", ans)
    #
    # ans_memo = solution.fib_memo(20)
    # print("ans_memo :", ans_memo)
    #
    # ans_dp_array = solution.fib_dp_array(20)
    # print("ans_dp_array :", ans_dp_array)
    #
    # ans_state_compression = solution.fib_state_compression(20)
    # print("ans_state_compression :", ans_state_compression)

    ans_matrix = solution.fib_matrix_power_series(20)
    print("ans :", ans_matrix)
