"""
给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。


示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。

提示：

1 <= text1.length, text2.length <= 1000
text1 和text2 仅由小写英文字符组成。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    # 自顶向下，递归
    # 时间复杂度：O()
    # 空间复杂度：O()
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[-1] * n for i in range(m)]
        def dp(text1, i, text2, j):
            # base case
            if i == m or j == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dp(text1, i+1, text2, j+1)
            else:
                memo[i][j] = max(dp(text1, i+1, text2, j),
                                 dp(text1, i, text2, j+1))
            return memo[i][j]
        return dp(text1, 0, text2, 0)

    # 时间复杂度：O(mn)
    # 空间复杂度：O(mn)
    def longestCommonSubsequence_iter(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for i in range(m+1)]
        # 定义：text1[0..i-1],text2[0..j-1]的lcs长度为dp[i][j]
        # 目标：text1[0..m-1],text2[0..n-1]的lcs长度为dp[m][n]
        # base case：dp[..][0] = dp[0][..] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    solution = Solution()
    res_recur = solution.longestCommonSubsequence(text1, text2)
    print('res_recur', res_recur)
    res_iter = solution.longestCommonSubsequence_iter(text1, text2)
    print('res_iter', res_iter)