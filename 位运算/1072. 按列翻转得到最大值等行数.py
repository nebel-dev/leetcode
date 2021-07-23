"""
给定由若干 0 和 1 组成的矩阵 matrix，从中选出任意数量的列并翻转其上的每个单元格。翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。

回经过一些翻转后，行与行之间所有值都相等的最大行数。

示例 1：

输入：[[0,1],[1,1]]
输出：1
解释：不进行翻转，有 1 行所有值都相等。
示例 2：

输入：[[0,1],[1,0]]
输出：2
解释：翻转第一列的值之后，这两行都由相等的值组成。
示例 3：

输入：[[0,0,0],[0,0,1],[1,1,0]]
输出：2
解释：翻转前两列的值之后，后两行由相等的值组成。

提示：

1 <= matrix.length <= 300
1 <= matrix[i].length <= 300
所有 matrix[i].length都相等
matrix[i][j] 为0 或1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flip-columns-for-maximum-number-of-equal-rows
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
from typing import List
arr1 = [[0,1],[1,1]]
arr2 = [[0,1],[1,0]]
arr3 = [[0,0,0],[0,0,1],[1,1,0]]

"""
思路：
两行各个位置的数字全部相同或全部相反，将每行的排列记作模式mode，模式相同才可以通过同时反转这两行的某些列使得各行中的数字完全一样，
用字典保存模式，
为了直观判断每行是否通过翻转列与其他行模式相同，令每行起始位为‘0’，不为‘0’的行每个位置取反，
最后遍历保存在字典中的模式，出现次数最多的模式为要求结果。
"""
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mode_freq = defaultdict(int)
        for row in matrix:
            mode = ""
            if row[0] == 0:
                mode = ''.join([str(c) for c in row])
            else:
                for c in row:
                    mode += ('0' if c == 1 else '1')
            mode_freq[mode] += 1
        return max(mode_freq.values())


solution = Solution()
r1 = solution.maxEqualRowsAfterFlips(arr3)

if __name__ == "__main__":
    print(r1)
