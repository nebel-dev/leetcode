"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

"""
class Solution:
    def singleNumber(self, nums):
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number

l = [4, 34, 34, 55, 4, 55, 678, 25, 678]
solution = Solution()
n = solution.singleNumber(l)

if __name__ == "__main__":
    print("single_number =", n)
