"""
集合 s 包含从 1 到n的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]

提示：

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-mismatch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List

l1 = [1, 2, 2, 4]
l2 = [1, 2, 5, 4, 5, 6]

# 数学方法
class Solution:
    def findErrorNums(self, nums: List[int]) -> int:
        s = sum(set(nums))
        return [sum(nums) - s, len(nums) * (len(nums) + 1) // 2 - s]
solution = Solution()
r1 = solution.findErrorNums(l1)

# 位运算方法
"""
重复数字记为dup，缺失数字记为miss
1.对数组所有元素以及1～n所有数进行异或，得到 dup^miss，记为mask，因为其余数字重复2次异或为0，
2.mask中值为1的位表示dup与miss不同的位（miss和dup一定不相等），将最右侧的那个不相同的位提取出来作为后面区分dup和miss的依据，记为bitmask，
3.提取方法：mask & (～mask + 1) <=> mask & ~(mask -1)，mask & ～mask = 0,且要取出的位置右侧全为0，通过～mask + 1后，要取的位右侧
还是0，且要取的位重新变为1，～mask + 1右侧与mask右侧取与后全置为0,左侧和mask中左侧相反，取与全置为0，这样就取出了dup和miss最右侧不相等的位。
4.现在要将dup和miss分开利用异或的性质（a^a=0，a^0=a）分别取出，将bitmask与数组所有元素与1～n取与，将结果为1和为0的数划分为2组，因为bitmask
表示dup和miss在这一位上不相等，因此dup和miss一定被划分在不同组，其中一组有3个dup，另一组有1个miss，将两组中的数相互异或，得到xor0,xor1,其中
一个是dup，另一个是miss，
5.此时分不清哪个是dup，需要遍历数组，在数组中的为dup，另一个就是miss。
"""
class Solution2:
    def findErrorNums(self, nums: List[int]) -> int:
        xor0, xor1, mask = 0, 0, 0
        for idx, num in enumerate(nums, 1):
            mask ^= idx ^ num
        bit_mask = mask & (~mask + 1)
        for idx, num in enumerate(nums, 1):
            if idx & bit_mask:
                xor1 ^= idx
            if num & bit_mask:
                xor1 ^= num
        xor0 = mask ^ xor1

        for num in nums:
            if xor0 == num:
                return [xor0, xor1]
            if xor1 == num:
                return [xor1, xor0]
solution2 = Solution2()
r2 = solution2.findErrorNums(l2)

# 哈希map
class Solution3:
    def findErrorNums(self, nums: List[int]) -> int:
        dup, miss = 0, 0
        dic = collections.Counter(nums)
        print(dic)
        for i in range(1, len(nums) + 1):
            if dic[i] == 2:
                dup = i
            if dic[i] == 0:
                miss = i
        return [dup, miss]
solution3 = Solution3()
r3 = solution3.findErrorNums(l2)

if __name__ == "__main__":
    print(r1)
    print(r2)
    print(r3)
