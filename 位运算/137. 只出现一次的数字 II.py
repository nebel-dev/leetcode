"""
给你一个整数数组nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

示例 1：

输入：nums = [2,2,3,2]
输出：3

示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99

提示：

1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List
l1 = [0, 1, 0, 1, 0, 1, 99]
l2 = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]

# 哈希表
class Solution:
    def single_number(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans
solution = Solution()
res1 = solution.single_number(l1)
res2 = solution.single_number(l2)

# 位运算
"""
python负数的存储方式是补码，但是想要以2进制输入-5，
要以-0b101形式，因为python整数没有位数限制，无法识别符号位，
所以-5的补码 0b11111011 会被当作正整数，
ans -= (1 << i)的目的是将负数的补码转换为 ”负号+原码” 的形式，这样python就可以正常识别2进制下的负数
"""
class Solution2:
    def single_number(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
s2 = Solution2()
r2 = s2.single_number(l2)

# 位运算
"""
因为python整数不限制位数，负数以补码形式存储
8位情况下-1的补码 0b11111111 不会被python识别为-1,而是识别为127
可以认为python的符号位在无限远处，而-1的补码应该是111...1111（无限多的1）
所以要执行 ~(res ^ 0xffffffff) 将0b11111111以外的位转换为1,这样才是在python内部的补码存储格式，
这样才能正确识别负数
"""
class Solution3:
    def single_number(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31-i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)
s3 = Solution3()
r4 = s3.single_number(l2)
if __name__ == "__main__":
    print("result =", res1, res2, r2, r4)
