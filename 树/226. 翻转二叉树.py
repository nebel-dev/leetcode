"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binaryTree_ser_deser import TreeNode, Codec


class Solution:
    # 前序遍历
    def invertTree_recur_pre(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        right = root.right
        root.right = self.invertTree_recur_pre(root.left)
        root.left = self.invertTree_recur_pre(right)
        return root

    # 中序遍历
    def invertTree_recur_in(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.invertTree_recur_in(root.left)
        right = root.right
        root.right = root.left
        root.left = right
        self.invertTree_recur_in(root.left)
        return root

    # 后序遍历
    def invertTree_recur_post(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.invertTree_recur_post(root.left)
        right = self.invertTree_recur_post(root.right)
        root.left = right
        root.right = left
        return root

    # 层序遍历
    # 看层序遍历的过程，有点像先序遍历
    def invertTree_bfs(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            right = node.right
            node.right = node.left
            node.left = right
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root


if __name__ == '__main__':
    data = "4,2,7,1,3,6,9"  # 层序遍历
    ser = Codec()
    deser = Codec()
    solution = Solution()
    root = deser.bfs_deserialize(data)

    # res = solution.invertTree_recur_post(root)
    res = solution.invertTree_bfs(root)
    res_str = ser.bfs_serialize(res)
    print(res_str)
