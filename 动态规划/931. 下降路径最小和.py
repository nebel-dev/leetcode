"""
给你一个 n x n 的 方形 整数数组matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者
向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

示例 1：

输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：下面是两条和最小的下降路径，用加粗标注：
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
示例 2：

输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：下面是一条和最小的下降路径，用加粗标注：
[[-19,57],
 [-40,-5]]
示例 3：

输入：matrix = [[-48]]
输出：-48

提示：

n == matrix.length
n == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dp(matrix, i, j):
            # 非法索引
            if i < 0 or j < 0 or i > len(matrix) or j > len(matrix):
                return 99999
            # base case
            if i == 0:
                return matrix[i][j]
            return matrix[i][j] + min(dp(matrix, i - 1, j - 1),
                                      dp(matrix, i - 1, j),
                                      dp(matrix, i - 1, j + 1))
        n = len(matrix)
        res = float('inf')

        for j in range(n):
            res = min(res, dp(matrix, n-1, j))
        return res

    # 时间复杂度：O(n^2)
    # 空间复杂度：O(1)
    def minFallingPathSum_iter(self, matrix: List[List[int]]) -> int:
        while len(matrix) >= 2:
            row = matrix.pop()
            for i in range(len(row)):
                matrix[-1][i] = matrix[-1][i] + min(row[max(0, i - 1): min(len(row), i + 2)])
        return min(matrix[0])


if __name__ == '__main__':
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    solution = Solution()
    res = solution.minFallingPathSum_iter(matrix)
    print("res :", res)
