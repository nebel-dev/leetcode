"""
给定一个非负整数num。对于0 ≤ i ≤ num 范围中的每个数字i，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的__builtin_popcount）来执行此操作。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
n1 = 2
n2 = 5
# 位运算
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            num = i
            for j in range(len(bin(num)) - 2 + 1):
                res[i] += num & 1
                num >>= 1
        return res
solution = Solution()
r1 = solution.countBits(n1)
r2 = solution.countBits(n2)

# 位运算 + 动态规划
"""
y = x & (x - 1)，表示将x的最低的1所在位变为0后的数，且0 <= y < x,显然y与x的1的数目相差1,
即 bits[x] = bits[y]+1，
即 bits[x] = bits[x & (x - 1)] + 1
遍历1～n的每个正整数i，计算bits值即可
"""
class Solution2:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            res.append(res[i & (i-1)] + 1)
        return res
solution2 = Solution2()
r3 = solution2.countBits(n1)
r4 = solution2.countBits(n2)

if __name__ == "__main__":
    print(r1, r2)
    print(r3, r4)
