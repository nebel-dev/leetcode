"""
给定两个单词word1和word2，找到使得word1和word2相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

提示：

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def longestCommonSubsequence_iter(text1: str, text2: str) -> int:
            m, n = len(text1), len(text2)
            dp = [[0] * (n + 1) for i in range(m + 1)]
            # 定义：text1[0..i-1],text2[0..j-1]的lcs长度为dp[i][j]
            # 目标：text1[0..m-1],text2[0..n-1]的lcs长度为dp[m][n]
            # base case：dp[..][0] = dp[0][..] = 0
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[m][n]
        m, n = len(word1), len(word2)
        lcs = longestCommonSubsequence_iter(word1, word2)
        return m + n - lcs * 2


if __name__ == '__main__':
    word1 = 'sea'
    word2 = 'eat'
    solution = Solution()
    res = solution.minDistance(word1, word2)
    print(res)