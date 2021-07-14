"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：

输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true

提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
l1 = [3, 9, 20, null, null, 15, 7]
l2 = [1, 2, 2, 3, 3, null, null, 4, 4]
l3 = []

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 自顶向下遍历
# 时间复杂度：O(n**2)
# 平均复杂度：O(n*log(n)),log(n)是平均情况下树的高度
# 类似前序遍历，对当前节点首先计算左右子树的高度，如果左右高度差不超过1,再分别递归遍历左右子节点，并判断左右子树是否平衡
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            else:
                return max(height(root.left), height(root.right)) + 1
        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.
                                                                                                                   right
                                                                                                                   )


# 自底向上遍历
# 时间复杂度：O(n)
# 类似后序遍历，对当前遍历到的节点，先判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡，如果一棵子树是平衡的，返回其高度，否则返回-1.
class Solution2:
    def isBalanced(self, root: TreeNode) ->bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1
        return height(root) >= 0

# 自底向上遍历
# 如果将左右子树高度的递归计算放在平衡的判断里，
# 这样左子树已经返回-1时就不需要再递归计算右子树了。


"""
自顶向下和自底向上的区别是什么？？？

关键就是先判断isBalanced(root->left)和isBalanced(root->right)是否成立，
还是先计算abs(height(root->left)-height(root->right)),前者就是自底而上，后者就是自顶而下？？？
如果是这样，那么上面自顶向下的方法中，return语句改为：
return self.isBalanced(root.left) and self.isBalanced(root.right）and abs(height(root.left) - height(root.right)) <= 1
这样能算自底向上么？不能吧？                                                   
"""


