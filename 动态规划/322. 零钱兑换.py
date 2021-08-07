"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。

你可以认为每种硬币的数量是无限的。


示例1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 暴力穷举
    # 时间复杂度：O(k^n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            return res if res != float('INF') else -1
        return dp(amount)

    # 可以用数组或哈希表（字典）记录要重复计算的节点值
    # 带备忘录的递归解法，自顶向下
    # 时间复杂度：O(n)
    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        def dp(n):
            # 返回备忘录中保存的值
            if n in memo:
                return memo[n]
            # base case
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res = min(res, subproblem + 1)
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        memo = {}
        return dp(amount)

    # 使用DP数组
    # 时间复杂度：O(n)
    def coinChange_dp_array(self, coins: List[int], amount: int) -> int:
        dp_array = [float('inf')] * (amount + 1)
        dp_array[0] = 0
        # for i in range(1, amount+1):
        #     for coin in coins:
        #         if i - coin < 0:
        #             continue
        #         dp_array[i] = min(dp_array[i], 1 + dp_array[i - coin])
        # for循环的另一种写法
        for coin in coins:
            for i in range(coin, amount + 1):
                dp_array[i] = min(dp_array[i], 1 + dp_array[i - coin])
        return dp_array[amount] if dp_array[amount] != float('inf') else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    solution = Solution()
    print(solution.coinChange(coins, 11))
    print(solution.coinChange_memo(coins, 11))
    print(solution.coinChange_dp_array(coins, 99))