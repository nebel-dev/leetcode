"""
给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time


class Solution:
    # 暴力递归
    def minDistance(self, word1: str, word2: str) -> int:
        # dp(i, j)表示word1[0..i]与word2[0..j]的最小编辑距离
        def dp(i, j):
            if i == -1:
                return j+1
            if j == -1:
                return i+1
            if word1[i] == word2[j]:
                return dp(i-1, j-1)  # 跳过
            else:
                return min(dp(i-1, j) + 1,  # 删除
                           dp(i, j-1) + 1,  # 插入
                           dp(i-1, j-1) + 1)  # 替换
        m, n = len(word1), len(word2)
        return dp(m-1, n-1)

    # 备忘录+递归
    def minDistance_memo(self, word1, word2):
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)  # 跳过
            else:
                memo[(i, j)] = min(dp(i - 1, j) + 1,  # 删除
                                   dp(i, j - 1) + 1,  # 插入
                                   dp(i - 1, j - 1) + 1)  # 替换
            return memo[(i, j)]
        m, n = len(word1), len(word2)
        memo = dict()
        return dp(m-1, n-1)

    # 迭代
    def minDistance_dp_array(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1 ]:
                    dp[i][j] = dp[i-1][j-1]  # 跳过
                else:
                    dp[i][j] = min(dp[i-1][j] + 1,  # 删除
                                   dp[i][j-1] + 1,  # 插入
                                   dp[i-1][j-1] + 1)  # 替换
        return dp[m][n]


if __name__ == "__main__":
    word1 = "intention"
    word2 = "execution"
    word3 = "dinitrophenylhydrazine"
    word4 = "benzalphenylhydrazone"
    word5 = "ap"
    word6 = "a"
    solution = Solution()

    time_1 = time.perf_counter()
    res = solution.minDistance(word1, word2)

    time_2 = time.perf_counter()
    res_memo = solution.minDistance_memo(word3, word4)

    time_3 = time.perf_counter()
    res_dp_array = solution.minDistance_dp_array(word3, word4)

    end = time.perf_counter()

    print(res, time_2-time_1)
    print(res_memo, time_3-time_2)
    print(res_dp_array, end-time_3)
